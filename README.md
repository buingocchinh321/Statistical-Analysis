# Statistical-Analysis
Using china-population.csv to visualize, PCA, LDA
I.	Thông tin về tập dữ liệu được chọn
Link: https://www.kaggle.com/datasets/anandhuh/population-data-china
1.	China Population:
-	Dân số Trung Quốc từ năm 1955 đến năm 2020 
-	Thông tin tập dữ liệu:
•	Year – Năm từ 2020 tới 1955
•	Population - Dân số trong năm tương ứng
•	Yearly % Change - Phần trăm thay đổi dân số hàng năm
•	Yearly Change - Thay đổi dân số hàng năm
•	Migrants (net) - Tổng số người di cư
•	Median Age - Tuổi trung bình của dân số
•	Fertility Rate - Tỷ lệ sinh
•	Density (P/Km²)- Mật độ dân số (dân số trên km vuông)
•	Urban Pop %- Phần trăm dân số thành thị
•	Urban Population- Dân số đô thị
•	Country's Share of World Pop - Tỷ lệ dân số
•	World Population - Dân số Thế giới trong năm tương ứng
•	China Global Rank - Xếp hạng toàn cầu về dân số
2.	China Population Forecast:
-	Dự đoán dân số TQ trong tương lai.
-	Thông tin tập dữ liệu giống China Population

II.	Trực quan hóa dữ liệu
1.	Bản đồ nhiệt về hệ số tương quan giữa các biến (correlations for multivariate data):
a.	Ý tưởng:
Dùng ma trận hệ số tương quan để vẽ lên thành 1 bản đồ nhiệt
b.	Hình ảnh:

 ![image](https://user-images.githubusercontent.com/63283198/165506872-e4bfff55-2fd1-440c-916c-b34a2bee6bf7.png)

2.	Bảng các thuộc tính có độ tương quan lớn nhất với nhau (most correlated):

 ![image](https://user-images.githubusercontent.com/63283198/165506907-00614123-2948-4fb0-8937-8aa6811e97e6.png)

3.	Nên giữ lại bao nhiêu thành phần chính
a.	Tính độ lệch chuẩn:

 ![image](https://user-images.githubusercontent.com/63283198/165506917-21a448ba-794e-4a5a-a5b0-3717ce0434a3.png)

b.	Trực quan hóa (đổi từ độ lệch chuẩn sang phương sai):

 ![image](https://user-images.githubusercontent.com/63283198/165506924-d11e68a2-4b62-4163-9880-e77d95215b38.png)

4.	Tổng dân số của TQ (gộp cả 2 tập dữ liệu):
a.	Ý tưởng:
Trục x: số năm
Trục y: dân số
b.	Hình ảnh:
 ![image](https://user-images.githubusercontent.com/63283198/165506939-861bdebe-7382-4b50-a241-28fa68cdb56f.png)

5.	Tỉ lệ thay đổi dân số theo năm (gộp cả 2 tập dữ liệu):
a.	Ý tưởng:
Trục x: số năm
Trục y: tỉ lệ tăng giảm
b.	Hình ảnh kết quả:
 ![image](https://user-images.githubusercontent.com/63283198/165506957-2428d028-2585-4792-bdf8-95bd5faa619e.png)

III.	Phân tích thành phần chính (Principal Components Analysis)
1.	Thư viện và hỗ trợ của thư viện:
Theo hướng dẫn thực hành thì em sử dụng Scikit learn, trong thư viện này có hỗ trợ tính PCA nhanh gọn chỉ bằng cách gọi module PCA có sẵn của thư viện. Việc duy nhất chúng ta cần chuẩn bị là tập dữ liệu và chuẩn hóa tập dữ liệu đó bằng hàm scale() cũng được hỗ trợ bởi Scikit luôn.
2.	Nhận xét
-	Bài tập được thực hiện nhanh gọn bằng thư viện.
-	Các module và hàm có sẵn đều có hướng dẫn trên trang chủ Scikit-Learn.
3.	Hình ảnh kết quả
 ![image](https://user-images.githubusercontent.com/63283198/165506967-8a775ac3-d7ae-4f96-9542-74dfe7bd53d3.png)

IV.	Phân tích phân biệt tuyến tính (Linear Discriminant Analysis)
1.	Thư viện và hỗ trợ thư viện
Cũng như PCA, LDA được hỗ trợ bởi Scikit-Learn, tập dữ liệu chuẩn bị cần chia thành X và Y. Với X là các thuộc tính cần xem xét phân tích, Y là mục tiêu hướng đến của phân tích đó. Ví dụ trong dataset China population trên, Y sẽ là xếp hạng dân số thế giới của TQ, trong khi đó, các thuộc tính còn lại sẽ là X.
2.	Nhận xét
-	Dễ sử dụng bằng thư viện.
3.	Hình ảnh kết quả
 ![image](https://user-images.githubusercontent.com/63283198/165506986-da03a778-b438-466a-97d4-69c6e61a382b.png)

