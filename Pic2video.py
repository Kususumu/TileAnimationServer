import cv2



class pic2Video:
    donePicSequenceCount = 0
    # raw Pic Sequence Path need to find in the mayaside:RenderScript Arnold Render function
    rawPicSequenceFolder = 'E:/mayaStore/images/imageSequence/'
    donePicSequenceFolder = "E:/mayaStore/images/outputSequence/"
    videoOutputPath = "E:/mayaStore/images/videoOutput/video.avi"
    backgroundPath = 'E:\\mayaStore\\images\\imageBackground\\image07.jpg'

    def rawPicSequence2FinalVideo(self,solvedTimeLine):
        # Use the sequenceRender to render the done Image Sequence
        self.donePicSequenceCount = self.sequenceRender(solvedTimeLine)

        self.finalVideo(self.getPicSize(), self.donePicSequenceCount)


    # We use the size , imageCount to make the final video
    def finalVideo(self,size, imageCount):
        picPath = self.donePicSequenceFolder
        videoPath = self.videoOutputPath

        fps = 24
        size = (size[1], size[0])
        videoWrite = cv2.VideoWriter(str(videoPath), cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)

        for i in range(imageCount):
            tFrame = cv2.imread(str(picPath) + 'CharacterImage_' + str(i) + '.png')
            print(str(picPath) + str(i) + '.png')
            videoWrite.write(tFrame)
            print('video i done' + str(i))

    # We use the number of motion and index of each motion to render the background image
    # We output how many image we create
    def sequenceRender(self,solvedTimeLine):
        solvedMotion = solvedTimeLine[0]
        solvedFrame = solvedTimeLine[3]
        background = self.readBackground()
        imageCount = 0
        # Read each motion
        for i in range(len(solvedMotion)):
            # Read each Frame
            for f in range(solvedFrame[i]):
                forePath = self.rawPicSequenceFolder \
                           + 'CharacterImage_' + str(i).zfill(2) + '_' + str(f).zfill(2) + '.png'

                outPath = self.donePicSequenceFolder
                self.alphaBlending(background, forePath, outPath, imageCount)

                imageCount += 1

        return imageCount

    # A function to get the picture size
    def getPicSize(self):
        backPath = self.backgroundPath
        background = cv2.imread(str(backPath))
        size = [background.shape[0], background.shape[1]]
        return size

    def readBackground(self):
        backPath = self.backgroundPath
        # Read the background images
        # background = cv2.imread("C:\\Users\\DELL\\Desktop\\aracimage\\backImage.png")
        background = cv2.imread(str(backPath))
        return background

    # forePath tell us where the location of the image Sequence output by maya
    # We use imageCount to save the index of the output Sequence
    def alphaBlending(self,background, forePath, outPath, imageCount):

        # Read foreground picture with the alpha
        # foregroundUnchange = cv2.imread("C:\\Users\\DELL\\Desktop\\aracimage\\man.png",cv2.IMREAD_UNCHANGED)
        foregroundUnchange = cv2.imread(str(forePath), cv2.IMREAD_UNCHANGED)
        foreground = foregroundUnchange[:, :, 0:3]
        alpha = foregroundUnchange[:, :, 3]

        # Convert uint8 to float
        foreground = foreground.astype(float)
        background = background.astype(float)

        uniRow = foreground.shape[0]
        uniCol = foreground.shape[1]

        # Normalize the alpha mask to keep intensity between 0 and 1
        alpha = alpha.astype(float) / 255

        # Multiply the foreground with the alpha matte
        for row in range(uniRow):
            for col in range(uniCol):
                foreground[row, col, 0] = alpha[row, col] * foreground[row, col, 0]
                foreground[row, col, 1] = alpha[row, col] * foreground[row, col, 1]
                foreground[row, col, 2] = alpha[row, col] * foreground[row, col, 2]

        # Multiply the background with ( 1 - alpha )
        # background = cv2.multiply(1.0 - alpha, background)
        for row in range(uniRow):
            for col in range(uniCol):
                background[row, col, 0] = (1 - alpha[row, col]) * background[row, col, 0]
                background[row, col, 1] = (1 - alpha[row, col]) * background[row, col, 1]
                background[row, col, 2] = (1 - alpha[row, col]) * background[row, col, 2]

        # Add the masked foreground and background.
        outImage = cv2.add(foreground, background)

        # Display image
        # cv2.imshow("outImg", outImage / 255)
        cv2.imwrite(str(outPath) + 'CharacterImage_' + str(imageCount) + '.png'.zfill(3), outImage)
        # cv2.waitKey(0)

# For Test
# alphaBlending(readBackground())