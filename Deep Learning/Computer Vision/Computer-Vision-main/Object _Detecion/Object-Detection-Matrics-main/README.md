# ファイル概要


### Ground Truth取得用ファイル
sequence_reader.ipynb

### 予測データ取得用ファイル
sequence_evaluation.py/ipynb

### 評価指標ファイル
model_eval.py/ipynb

### AP評価判定ファイル
evaluation.ipynb



# 使い方

### おおまかな手順
1. 各解像度の正解データを取得、保存
2. 各解像度の予測データの取得、保存
3. 評価指標ファイルをインポート
4. 保存された正解データ、予測データよりAP測定 

<br />
<br />





## 1.各解像度の正解データを取得、保存
sequence_reader.ipynb内にて、\
Folderクラスの定義 
```python
class Folder():
    def __init__(self, folder):
        """
        Input:
            folder: path to the folder with images 
        
        Attributes:
            path: input path passed as argument
            len: lengh of directory of input path
            images: list of path of images in the folder
         """
            
        self.path = os.path.join(os.getcwd(), folder)
        self.len = len(os.listdir(self.path))
        self.images = list(os.listdir(self.path))
    
    def visualize(self):
        plt.figure(figsize=(12, 8))
        for index, i in enumerate(self.images):
            image = os.path.join(self.path, i)
            if self.len%2 ==0:
                x, y = int(self.len/2), int(self.len/2)
            else:
                x, y = int(self.len/2) + 1, int(self.len/2)
            plt.subplot(x, y, index + 1)
            image = plt.imread(image)
            plt.imshow(image)
            plt.title('00000{}\n'.format(index+1), fontsize = 10)
            plt.tight_layout()        
        
    def reset(self):
        self.currentDigit = 0
    
    def __iter__(self):
        self.currentDigit = 0
        return self
    
    def __next__(self):
        self.currentDigit+=1 # Initialize iteration by adding 1
        if self.currentDigit <= self.len: # Check if the current number is within a length
            image_n = str(self.currentDigit).zfill(6) + ".jpg" #この部分をファイル名に従い変更
            path = os.path.join(self.path, image_n)
            if Path(path).exists(): # Check if the path exists
                return path
            else:
                print("Reach the maximum length")
                raise StopIteration

    def __len__(self):
        return self.len
```

引数に画像が保存されているフォルダパスを指定
```python
venice = Folder("venice") #フォルダのパスを指定
```
Ground Truthの取得
```python
ground_truth = pd.read_csv("images/venice.txt", delimiter=",", header=None)
ground_truth = ground_truth[[0, 2,3,4,5,6]]
ground_truth.rename(columns={ 0:"frame", 2:"x", 3:"y", 4:"w", 5:"h", 6:"score"}, inplace=True)
```

座標変換 
```python
ground_truth["x1"] = ground_truth.x
ground_truth["y1"] = ground_truth.y
ground_truth["x2"] = (ground_truth.x + ground_truth.w)
ground_truth["y2"] = (ground_truth.y + ground_truth.h)
```

各解像度へスケーリング
```python
x_scale =  940/1920　#希望サイズ/元サイズ
y_scale =  540/1080　#希望サイズ/元サイズ

ground_truth["x1_scaled"] = (np.round(ground_truth.x1 * x_scale)).astype(int)
ground_truth["y1_scaled"] = (np.round(ground_truth.y1 * y_scale)).astype(int)
ground_truth["x2_scaled"] = (np.round(ground_truth.x2 * x_scale)).astype(int)
ground_truth["y2_scaled"] = (np.round(ground_truth.y2 * y_scale)).astype(int)   
```

Ground Truthの可視化、確認
```python
# Capture video from file
index=1
for image in venice:
    if image:
        frame = np.asarray(Image.open(image))
        frame = cv2.resize(frame, (940, 540))
        boxes_scaled=ground_truth[ground_truth["frame"]==index]["x1_scaled y1_scaled x2_scaled y2_scaled".split(" ")].values
        for box in boxes_scaled.tolist():
            left, top, width, height= box
            #print(frame, box)
            #print(resize_image(frame, [box], 940, 540))
            #pt1=(int(left),int(top))
            #pt2=(int(left+width), int(top+height))
            cv2.rectangle(frame, (int(left), int(top)), (int(width), int(height)), (255,255,255), 2)   
        cv2.imshow('frame',frame)
        index+=1
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break
```

確認完了後、保存
```python
ground_truth.to_csv("venice_groundtruth_940_540.csv", index=False)
```

## 2. 各解像度の予測データの取得、保存



<取得データ例>
|  frame  |  x  | y | w | h | scores |
| ----    | ----|---|---|---|  ----  |
|  1      | 1835|401|83 |249|0.99345 |
|  1      | 1253|438|43 |106|0.98621 |
|  1      | 1454|450|144|324|0.98034 |
|  2      | 1370|440|31 |54 |0.99488 |
|  2      | 1458|443|137|335|0.98636 |


引数に画像が保存されているフォルダパスを指定
```python
venice = Folder("venice") #フォルダのパスを指定
```

予測ファイル定義
```python
box_list=pd.DataFrame(columns=["frame", "x", "y","w","h", "scores"])
```

各フレーム取得、解像度変更後推論
```python
    index = 1
    for image in venice:
        if image:
            frame = np.asarray(Image.open(image))
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Display the resulting frame
            t1 = time.time() #Start 
            frame = cv2.resize(frame, (1920, 1080)) #解像度変更
            image = Image.fromarray(frame[...,::-1]) #bgr to rgb
            boxs, class_names, raw_scores = yolo.detect_image(image)
            features = encoder(frame,boxs)    
            #class_list.append(list(itertools.chain.from_iterable(class_names)))
            detections = [Detection(bbox, scores, feature) for bbox, scores, feature in zip(boxs, raw_scores, features)]
            # Run non-maxima suppression.
            boxes = np.array([d.tlwh for d in detections])       
            scores = np.array([d.confidence for d in detections]) #NMX後は全て１になっている  
```

box_list(予測ファイル)へ各フレーム毎の推論結果を追加
```python
            if len(np.vstack([np.repeat(index, boxes.shape[0]), boxes.T, scores]).T)>0:
                box_list=box_list.append(pd.DataFrame(np.vstack([np.repeat(index, boxes.shape[0]), boxes.T, scores]).T, 
                                                      columns=["frame", "x", "y","w","h","scores"]))
            else:
                continue
```

ループ終了後、確認・保存
```python
box_list.to_csv("evaluation_data/venice_tiny_yolov3_fixed2_1920_1080.csv", index=False) #各解像度ごとにファイル名を変更
```


## 3. 評価指標ファイルをインポート

### 評価指標ファイル内容一覧

- バウンディングボクス座標変換関数
```python
def box_corner_to_center(boxes):
    """Convert from (upper-left, lower-right) to (center, width, height)."""
    x1, y1, x2, y2 = boxes[0], boxes[1], boxes[2], boxes[3]
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    w = x2 - x1
    h = y2 - y1
    boxes = np.stack((cx, cy, w, h), axis=-1)
    return boxes

def box_center_to_corner(boxes):
    """Convert from (center, width, height) to (upper-left, lower-right)."""
    cx, cy, w, h = boxes[0], boxes[1], boxes[2], boxes[3]
    x1 = cx - 0.5 * w
    y1 = cy - 0.5 * h
    x2 = cx + 0.5 * w
    y2 = cy + 0.5 * h
    boxes = np.stack((x1, y1, x2, y2), axis=-1)
    return boxes
```
- バウンディングボクスの信頼度取得
```python
def get_model_scores(pred_boxes):
    """Creates a dictionary of from model_scores to image ids.
    Args:
        pred_boxes (dict): dict of dicts of 'boxes' and 'scores'
    Returns:
        dict: keys are model_scores and values are image ids (usually filenames)
    """
    model_score={}
    for img_id, val in pred_boxes.items():
        for score in val['scores']:
            if score not in model_score.keys():
                model_score[score]=[img_id]
            else:
                model_score[score].append(img_id)
    return model_score
```

- IOU(Intersection Over Union)計算
```python
def calc_iou( gt_bbox, pred_bbox):
    '''
    This function takes the predicted bounding box and ground truth bounding box and 
    return the IoU ratio
    '''
    x_topleft_gt, y_topleft_gt, x_bottomright_gt, y_bottomright_gt= gt_bbox
    x_topleft_p, y_topleft_p, x_bottomright_p, y_bottomright_p= pred_bbox
    

         
    #if the GT bbox and predcited BBox do not overlap then iou=0
    if(x_bottomright_gt< x_topleft_p):
        # If bottom right of x-coordinate  GT  bbox is less than or above the top left of x coordinate of  the predicted BBox
       
        return 0.0
    if(y_bottomright_gt< y_topleft_p):  # If bottom right of y-coordinate  GT  bbox is less than or above the top left of y coordinate of  the predicted BBox
        
        return 0.0
    if(x_topleft_gt> x_bottomright_p): # If bottom right of x-coordinate  GT  bbox is greater than or below the bottom right  of x coordinate of  the predcited BBox
        
        return 0.0
    if(y_topleft_gt> y_bottomright_p): # If bottom right of y-coordinate  GT  bbox is greater than or below the bottom right  of y coordinate of  the predcited BBox
        
        return 0.0
    
    GT_bbox_area = (x_bottomright_gt -  x_topleft_gt + 1) * (  y_bottomright_gt -y_topleft_gt + 1)
    Pred_bbox_area =(x_bottomright_p - x_topleft_p + 1 ) * ( y_bottomright_p -y_topleft_p + 1)
    
    x_top_left =np.max([x_topleft_gt, x_topleft_p])
    y_top_left = np.max([y_topleft_gt, y_topleft_p])
    x_bottom_right = np.min([x_bottomright_gt, x_bottomright_p])
    y_bottom_right = np.min([y_bottomright_gt, y_bottomright_p])
    
    intersection_area = (x_bottom_right- x_top_left + 1) * (y_bottom_right-y_top_left  + 1)
    
    union_area = (GT_bbox_area + Pred_bbox_area - intersection_area)
   
    return intersection_area/union_area
```

- Precision, Recall計算
```python
def calc_precision_recall(image_results):
    """Calculates precision and recall from the set of images
    Args:
        img_results (dict): dictionary formatted like:
            {
                'img_id1': {'true_pos': int, 'false_pos': int, 'false_neg': int},
                'img_id2': ...
                ...
            }
    Returns:
        tuple: of floats of (precision, recall)
    """
    true_positive=0
    false_positive=0
    false_negative=0
    for img_id, res in image_results.items():
        true_positive +=res['true_positive']
        false_positive += res['false_positive']
        false_negative += res['false_negative']
        try:
            precision = true_positive/(true_positive+ false_positive)
        except ZeroDivisionError:
            precision=0.0
        try:
            recall = true_positive/(true_positive + false_negative)
        except ZeroDivisionError:
            recall=0.0
    return (precision, recall)
```
- 各画像における結果の出力
```python
def get_single_image_results(gt_boxes, pred_boxes, iou_thr):
    """Calculates number of true_pos, false_pos, false_neg from single batch of boxes.
    Args:
        gt_boxes (list of list of floats): list of locations of ground truth
            objects as [xmin, ymin, xmax, ymax]
        pred_boxes (dict): dict of dicts of 'boxes' (formatted like `gt_boxes`)
            and 'scores'
        iou_thr (float): value of IoU to consider as threshold for a
            true prediction.
    Returns:
        dict: true positives (int), false positives (int), false negatives (int)
    """
    all_pred_indices= range(len(pred_boxes))
    all_gt_indices=range(len(gt_boxes))
    if len(all_pred_indices)==0:
        tp=0
        fp=0
        fn=0
        return {'true_positive':tp, 'false_positive':fp, 'false_negative':fn}
    if len(all_gt_indices)==0:
        tp=0
        fp=0
        fn=0
        return {'true_positive':tp, 'false_positive':fp, 'false_negative':fn}
    
    gt_idx_thr=[]
    pred_idx_thr=[]
    ious=[]
    for ipb, pred_box in enumerate(pred_boxes):
        for igb, gt_box in enumerate(gt_boxes):
            iou= calc_iou(gt_box, pred_box)
            if iou >iou_thr:
                gt_idx_thr.append(igb)
                pred_idx_thr.append(ipb)
                ious.append(iou)
    iou_sort = np.argsort(ious)[::1]
    
    if len(iou_sort)==0:
        tp=0
        fp=0
        fn=0
        return {'true_positive':tp, 'false_positive':fp, 'false_negative':fn}
    else:
        gt_match_idx=[]
        pred_match_idx=[]
        for idx in iou_sort:
            gt_idx=gt_idx_thr[idx]
            pr_idx= pred_idx_thr[idx]
            # If the boxes are unmatched, add them to matches
            if(gt_idx not in gt_match_idx) and (pr_idx not in pred_match_idx):
                gt_match_idx.append(gt_idx)
                pred_match_idx.append(pr_idx)
        tp= len(gt_match_idx)
        fp= len(pred_boxes) - len(pred_match_idx)
        fn = len(gt_boxes) - len(gt_match_idx)
    return {'true_positive': tp, 'false_positive': fp, 'false_negative': fn}
```

- AP計算
```python
def get_avg_precision_at_iou(gt_boxes, pred_bb, iou_thr=0.5):
    
    model_scores = get_model_scores(pred_bb)
    sorted_model_scores= sorted(model_scores.keys())
    # Sort the predicted boxes in descending order (lowest scoring boxes first):
    for img_id in pred_bb.keys():   
        arg_sort = np.argsort(pred_bb[img_id]['scores'])
        pred_bb[img_id]['scores'] = np.array(pred_bb[img_id]['scores'])[arg_sort].tolist()
        pred_bb[img_id]['boxes'] = np.array(pred_bb[img_id]['boxes'])[arg_sort].tolist()
    pred_boxes_pruned = deepcopy(pred_bb)

    precisions = []
    recalls = []
    model_thrs = []
    img_results = {}
    print(pred_bb.keys())
    # Loop over model score thresholds and calculate precision, recall
    for ithr, model_score_thr in enumerate(sorted_model_scores[:-1]):
            # On first iteration, define img_results for the first time:
        #print("Mode score : ", model_score_thr)
        #img_ids = gt_boxes.keys() if ithr == 0 else model_scores[model_score_thr] #変更前
        img_ids = pred_bb.keys() if ithr == 0 else model_scores[model_score_thr] #変更後
        for img_id in img_ids:   
            gt_boxes_img = gt_boxes[img_id]
            box_scores = pred_boxes_pruned[img_id]['scores']
            start_idx = 0
            for score in box_scores:
                if score <= model_score_thr:
                    pred_boxes_pruned[img_id]
                    start_idx += 1
                else:
                    break 
            # Remove boxes, scores of lower than threshold scores:
            pred_boxes_pruned[img_id]['scores']= pred_boxes_pruned[img_id]['scores'][start_idx:]
            pred_boxes_pruned[img_id]['boxes']= pred_boxes_pruned[img_id]['boxes'][start_idx:]
            # Recalculate image results for this image
            img_results[img_id] = get_single_image_results(gt_boxes_img["boxes"], pred_boxes_pruned[img_id]['boxes'], iou_thr)
        # calculate precision and recall
        prec, rec = calc_precision_recall(img_results)
        precisions.append(prec)
        recalls.append(rec)
        model_thrs.append(model_score_thr)
    precisions = np.array(precisions)
    recalls = np.array(recalls)
    prec_at_rec = []
    for recall_level in np.linspace(0.0, 1.0, 11):
        try:
            args= np.argwhere(recalls>recall_level).flatten()
            prec= max(precisions[args])
            #print(recalls,"Recall")
            #print(      recall_level,"Recall Level")
            #print(       args, "Args")
            #print(       prec, "precision")
        except ValueError:
            prec=0.0
        prec_at_rec.append(prec)
    avg_prec = np.mean(prec_at_rec) 
    return {
        'avg_prec': avg_prec,
        'precisions': np.mean(precisions),
        'recalls': np.mean(recalls),
        #'model_thrs': model_thrs
        }
```
評価指標インポート
```python
from model_eval import box_center_to_corner, box_corner_to_center, get_avg_precision_at_iou, get_model_scores, get_single_image_results
```

## 4. 保存された正解データ、予測データよりAP測定

正解データ
```python
ground_truth = pd.read_csv("evaluation/venice_groundtruth_1920_1080.csv")
```

辞書型へ変換
```python
gt_dict = {}
for i, df in ground_truth.groupby("frame"):
    gt_dict[i] = dict(boxes = (df["x1 y1 x2 y2".split(" ")].values).astype(int).tolist())
```

予測データ
```python
pred_dict = pd.read_csv("evaluation_data/venice_tiny_yolov3_fixed2_1920_1080.csv") 
#座標変換
pred_dict["x1"] = pred_dict.x
pred_dict["y1"] = pred_dict.y
pred_dict["x2"] = pred_dict.x + pred_dict.w
pred_dict["y2"] = pred_dict.y + pred_dict.h
```

辞書型へ変換
```python
predict = {}
for i, df in pred_dict.groupby("frame"):
    predict[int(i)] = dict(boxes = (df["x1 y1 x2 y2".split(" ")].values).astype(int).tolist(),
                      scores = df.scores.values.tolist())    
```

AP測定
```python
get_avg_precision_at_iou(gt_dict, predict, iou_thr=0.5)
```