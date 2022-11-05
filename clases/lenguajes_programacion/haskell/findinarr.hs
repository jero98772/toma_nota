-- find x tree times in array
find n a = n `elem` a

findntimes t n a = replicate t find n a  