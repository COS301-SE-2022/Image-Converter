import cv2
import numpy as np
"""converter."""
from converter.resizing import imageResizing
from converter.watermark import AddMark
from PIL import Image
import torch
from basicsr.archs.rrdbnet_arch import RRDBNet

import sys
sys.path.append('../')

class smoothing:
    def __init__(self,uploaded_image):
        self.img = uploaded_image

    def clean_noise(self):
        ########################################################################
        model_path = 'converter/RealESRGAN_x4plus.pth'
        img_path = '/Users/neoseefane/Documents/GitHub/Image-Converter/Server/converter/imageSmoothing/download_1.png'

        # initialize gpu acceleration
        if torch.backends.mps.is_available():
            device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
        else:
            device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32)
        loadnet = torch.load(model_path)
        if 'params_ema' in loadnet:
            keyname = 'params_ema'
        else:
            keyname = 'params'
        model.load_state_dict(loadnet[keyname], strict=True)
        model.eval()
        model = model.to(device)
        print('Model path {:s}. \nTesting...'.format(model_path))

        # img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED).astype(np.float32)
        
        img = cv2.imread(self.img,  cv2.IMREAD_UNCHANGED).astype(np.float32)
        # img = self.img
        # cv2.imshow("Image: ", img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # os.makedirs('results/', exist_ok=True)

        if np.max(img) > 255:  # 16-bit image
            max_range = 65535
            print('\tInput is a 16-bit image')
        else:
            max_range = 255
        img = img / max_range
        if len(img.shape) == 2:  # gray image
            img_mode = 'L'
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        elif img.shape[2] == 4:  # RGBA image with alpha channel
            img_mode = 'RGBA'
            alpha = img[:, :, 3]
            img = img[:, :, 0:3]
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # if args.alpha_upsampler == 'realesrgan':
            #     alpha = cv2.cvtColor(alpha, cv2.COLOR_GRAY2RGB)
        else:
            img_mode = 'RGB'
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img1 = img
        img = torch.from_numpy(np.transpose(img[:, :, [2, 1, 0]], (2, 0, 1))).float()
        img = img.unsqueeze(0).to(device)

        with torch.no_grad():
            output = model(img).data.squeeze().float().cpu().clamp_(0, 1).numpy()
        output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))
        output1 =  Image.fromarray((output * 255).astype(np.uint8))
     
        output1 = np.array(output1)
        output1 = output1[:, :, ::-1].copy()
       
        ########################################################################
     
        resizedImage = imageResizing(output1)
        resizedImage = resizedImage.resize()
        print('Resized image:', resizedImage.shape)
        
        print(resizedImage.__class__)
        imageWatermark = AddMark(Image.fromarray(cv2.cvtColor(resizedImage, cv2.COLOR_BGR2RGB)))


        imageWatermark = imageWatermark.Dev()
        imageWatermark.show()
        imageWatermark= np.array(imageWatermark) 
    
        imageWatermark = imageWatermark[:, :, ::-1].copy() 

        cv2.imwrite("images/original/Graph.png", imageWatermark)
        return imageWatermark

if __name__ == '__main__':
    obj = smoothing('imageSmoothing/img.png')
    img = obj.clean_noise()
    # cv2.imshow("Original: ", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    # src = ['/Users/neoseefane/Documents/GitHub/Image-Converter/Server/images/download.png']
    # for i in src:
    #     img = Image.open(i)
    #     img = cv2.imread(i)
    #     open_cv_image = np.array(img)
    #     # Convert RGB to BGR
    #     open_cv_image = open_cv_image[:, :, ::-1].copy()
    #     object = smoothing(open_cv_image)
    #     object.clean_noise()
    #     break
"""
@InProceedings{wang2021realesrgan,
    author    = {Xintao Wang and Liangbin Xie and Chao Dong and Ying Shan},
    title     = {Real-ESRGAN: Training Real-World Blind Super-Resolution with Pure Synthetic Data},
    booktitle = {International Conference on Computer Vision Workshops (ICCVW)},
    date      = {2021}
}
"""