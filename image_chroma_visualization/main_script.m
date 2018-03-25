%Script to generate chroma-histogram on a linear input image


file_names = ["test_img1.png", "test_img2.png", "test_img3.png", "test_image4.jpg"]

%Read image file given a list of file_name in current directory

for i_file = 1:length(file_names)
  file_name = file_names{i_file};
  fprintf("Processing %s\n", file_name);
  I_linear = imread(file_name);
  image(I_linear)
  I_valid = all(I_linear > 0,3);
  X = FeaturizeImage(I_linear, I_valid);
  X_vis = bsxfun(@rdivide, double(X), max(max(X, [], 1), [], 2));
  figure(1)
  imagesc(X_vis); axis image off
  title('Histograms')
  drawnow;
end
