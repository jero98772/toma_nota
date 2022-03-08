path <- "~/pathToFowardAndReverse"
fnFs <- sort(list.files(path, pattern ="_R1_001__V[0-2].fastq" ,full.names = TRUE))
fnRs <- sort(list.files(path, pattern="_R2_001__V[0-9].fastq", full.names = TRUE))
sample.names <- sapply(strsplit(basename(fnFs), "_"), `[`, 9)
sample.names <- sapply(strsplit(basename(fnRs), "_"), `[`, 9)
#plotQualityProfile(fnFs[1:2])

errF <- learnErrors(fnFs, multithread=TRUE)
errR <- learnErrors(fnRs, multithread=TRUE)
#plotErrors(errF, nominalQ=TRUE)

# derep object has the reads and uniques sequences
derepFs <- derepFastq(fnFs, verbose=TRUE)
# dada object has the inferred variants from unique sequences
dadaFs <- dada(derepFs, err=errF, multithread=TRUE, OMEGA_C=0)

# Returns the index of values that are TRUE in the comparison
# In that way, we can know which unique sequence in derepFs 
# is associate to the abundance of certain dadaFs denoised sequences
which(dadaFs$map==1)
which(dadaFs$map==2)