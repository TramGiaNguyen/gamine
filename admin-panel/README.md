# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

# Admin Panel

Đây là ứng dụng Admin Panel cho cửa hàng Gamine, được xây dựng bằng React và TypeScript.

## Cài đặt

1. Clone repository
2. Cài đặt dependencies:
   ```
   npm install
   ```
3. Khởi chạy ứng dụng:
   ```
   npm start
   ```

## Cấu hình Cloudinary để tải lên hình ảnh sản phẩm

Ứng dụng sử dụng Cloudinary như một dịch vụ lưu trữ hình ảnh miễn phí. Để thiết lập:

1. Đăng ký tài khoản miễn phí tại [Cloudinary](https://cloudinary.com/users/register/free)
2. Sau khi đăng nhập, truy cập Dashboard để lấy thông tin:
   - Cloud name: Hiển thị ở góc trên bên phải
   - API Key và API Secret: Tab Settings > Security

3. Tạo một Upload Preset:
   - Đi đến Settings > Upload
   - Tìm đến phần "Upload presets" và nhấn "Add upload preset"
   - Đặt Signing Mode là "Unsigned"
   - Đặt Preset name là "gamine_preset" (hoặc tên bạn muốn)
   - Lưu các thay đổi

4. Cập nhật file cấu hình trong ứng dụng:
   - Mở file `src/pages/ProductManagement.tsx`
   - Cập nhật các biến sau:
     ```javascript
     const CLOUDINARY_UPLOAD_PRESET = 'gamine_preset'; // hoặc tên preset bạn đã tạo
     const CLOUDINARY_CLOUD_NAME = 'your_cloud_name'; // thay bằng cloud name của bạn
     ```

5. Kiểm tra kết nối:
   - Khởi chạy ứng dụng
   - Tạo một sản phẩm mới và thử tải lên hình ảnh

## Sử dụng

1. Đăng nhập bằng tài khoản admin
2. Quản lý người dùng, sản phẩm, danh mục, đơn hàng và các chức năng khác
3. Xem thống kê trên Dashboard

## Tính năng chính

- Xác thực và ủy quyền
- Quản lý người dùng
- Quản lý sản phẩm và danh mục
- Quản lý đơn hàng
- Quản lý khuyến mãi
- Báo cáo và thống kê
