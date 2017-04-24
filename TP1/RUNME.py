import PSpy


inputDirectory = "../img/"
resultsDirectory = "../res/"

averagePSResultsFileName = resultsDirectory + "averagePS.hdf5"
averagePSFigureFileName = resultsDirectory + "averagePS.png"

averagePSLocalResultsFileName = resultsDirectory + "averagePSLocal.hdf5"
averagePSLocalFigureFileName = resultsDirectory + "averagePSLocal.png"

sampleSize = [64, 64]
gridSize = [3, 3]


averagePS = PSpy.getAveragePS(inputDirectory, sampleSize)

PSpy.saveH5(averagePSResultsFileName,'averagePS',averagePS)
PSpy.makeAveragePSFigure(averagePS, averagePSFigureFileName)

# averagePSRadial = PSpy.getRadialPS(averagePS)
# radialFreq = PSpy.getRadialFreq(averagePS.shape)
# PSpy.saveH5(averagePSRadialResultsFileName,'averagePSRadial',averagePSRadial)
# PSpy.makeAveragePSRadialFigure(radialFreq,averagePSRadial, averagePSRadialFigureFileName)
#
# averagePSLocal = PSpy.getAveragePSLocal(inputDirectory, sampleSize, gridSize)
# PSpy.saveH5(averagePSLocalResultsFileName,'averagePS',averagePSLocal)
# PSpy.makeAveragePSLocalFigure(averagePSLocal, averagePSLocalFigureFileName,gridSize)