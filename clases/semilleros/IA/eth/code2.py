def entropy_feautre(signal):
    f, psd = scs.periodogram(signal)
    # Calculate the entropy from the PSD
    #entropy = -np.sum(psd * np.log2(psd))
    if psd.all() != 0:
        entropy = -np.sum(psd * np.log2(psd))
    else:
        entropy = 0
    return entropy

def RMS(signal):
    # RMS = sqrt(1/N*sum(x_i^2)) 
    RMS = np.sqrt(np.mean(np.square(signal)))
    return RMS

def percentile_75(signal):
    per_75 = np.percentile(signal, 75)
    return per_75

def Inter_quartile_range(signal):
    per_75 = np.percentile(signal, 75)
    per_25 = np.percentile(signal, 25)
    diff = per_75 - per_25
    return diff

def smart_wart_location_test (trace, classifier):
    
    wind_size = 400
    wind_samples = 400

    test_dict_features={'RMS_x':[] , 'RMS_y':[] , 'RMS_z':[] , '75_perc_x': [],  '75_perc_y': [],  '75_perc_z': [],'Int_Quart_range_x': [] , 'Int_Quart_range_y': [] , 'Int_Quart_range_z': [] , 'Entropy_x': [], 'Entropy_y': [],'Entropy_z': []} #, 'Frequency_x': [], 'Frequency_y': [],'Frequency_z': [] }
    #dict_features={'RMS_x':[] , 'RMS_y':[] , 'RMS_z':[] , '75_perc_x': [],  '75_perc_y': [],  '75_perc_z': [],'Int_Quart_range_x': [] , 'Int_Quart_range_y': [] , 'Int_Quart_range_z': [] , 'Entropy_x': [], 'Entropy_y': [],'Entropy_z': [], 'Frequency_x': [], 'Frequency_y': [],'Frequency_z': [] }

    fs = trace.data['ax'].samplerate
    ax = trace.data['ax'].values
    ay = trace.data['ay'].values
    az = trace.data['az'].values


    for s in range(0, len(ax)-wind_size,wind_samples):

        ax_win = ax[s:s+wind_size]
        ay_win = ay[s:s+wind_size]
        az_win = az[s:s+wind_size]

        test_dict_features['RMS_x']+=[RMS(ax_win)]
        test_dict_features['RMS_y']+=[RMS(ay_win)]
        test_dict_features['RMS_z']+=[RMS(az_win)]

        test_dict_features['75_perc_x']+=[percentile_75(ax_win)]
        test_dict_features['75_perc_y']+=[percentile_75(ay_win)]
        test_dict_features['75_perc_z']+=[percentile_75(az_win)]

        test_dict_features['Int_Quart_range_x']+=[Inter_quartile_range(ax_win)]
        test_dict_features['Int_Quart_range_y']+=[Inter_quartile_range(ay_win)]
        test_dict_features['Int_Quart_range_z']+=[Inter_quartile_range(az_win)]

        test_dict_features['Entropy_x']+=[entropy_feautre(ax_win)]
        test_dict_features['Entropy_y']+=[entropy_feautre(ay_win)]
        test_dict_features['Entropy_z']+=[entropy_feautre(az_win)]
        
        
    # make prediciton with trained classifier for each window
    location_features = pd.DataFrame.from_dict(test_dict_features)
    test_preds = classifier.predict(location_features)

    # get most common in trace overall windows
    location = mode(test_preds)

    return location