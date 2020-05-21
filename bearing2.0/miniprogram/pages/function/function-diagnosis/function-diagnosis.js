// pages/function/function-diagnosis/function-diagnosis.js
var util = require('../../../utils/util.js');
var app = getApp();
Page({
  /**
   * 页面的初始数据
   */
  data: {
    time: '',
    array: ['设备100-TEST1.csv', '设备100-TEST2.csv', '设备100-TEST3.csv', '设备100-TEST4.csv', '设备100-TEST5.csv', '设备100-TEST6.csv', '设备100-TEST7.csv', '设备100-TEST8.csv', '设备100-TEST9.csv', '设备100-TEST10.csv', '设备108-TEST11.csv', '设备108-TEST12.csv', '设备108-TEST13.csv', '设备108-TEST14.csv', '设备108-TEST15.csv', '设备108-TEST16.csv', '设备108-TEST17.csv', '设备108-TEST18.csv', '设备108-TEST19.csv', '设备108-TEST20.csv', '设备121-TEST21.csv', '设备121-TEST22.csv', '设备121-TEST23.csv', '设备121-TEST24.csv', '设备121-TEST25.csv', '设备121-TEST26.csv', '设备121-TEST27.csv', '设备121-TEST28.csv', '设备121-TEST29.csv', '设备121-TEST30.csv', '设备133-TEST31.csv', '设备133-TEST32.csv', '设备133-TEST33.csv', '设备133-TEST34.csv', '设备133-TEST35.csv', '设备133-TEST36.csv', '设备133-TEST37.csv', '设备133-TEST38.csv', '设备133-TEST39.csv', '设备133-TEST40.csv', '设备147-TEST41.csv', '设备147-TEST42.csv', '设备147-TEST43.csv', '设备147-TEST44.csv', '设备147-TEST45.csv', '设备147-TEST46.csv', '设备147-TEST47.csv', '设备147-TEST48.csv', '设备147-TEST49.csv', '设备147-TEST50.csv', '设备160-TEST51.csv', '设备160-TEST52.csv', '设备160-TEST53.csv', '设备160-TEST54.csv', '设备160-TEST55.csv', '设备160-TEST56.csv', '设备160-TEST57.csv', '设备160-TEST58.csv', '设备160-TEST59.csv', '设备160-TEST60.csv', '设备172-TEST61.csv', '设备172-TEST62.csv', '设备172-TEST63.csv', '设备172-TEST64.csv', '设备172-TEST65.csv', '设备172-TEST66.csv', '设备172-TEST67.csv', '设备172-TEST68.csv', '设备172-TEST69.csv', '设备172-TEST70.csv', '设备188-TEST71.csv', '设备188-TEST72.csv', '设备188-TEST73.csv', '设备188-TEST74.csv', '设备188-TEST75.csv', '设备188-TEST76.csv', '设备188-TEST77.csv', '设备188-TEST78.csv', '设备188-TEST79.csv', '设备188-TEST80.csv', '设备200-TEST81.csv', '设备200-TEST82.csv', '设备200-TEST83.csv', '设备200-TEST84.csv', '设备200-TEST85.csv', '设备200-TEST86.csv', '设备200-TEST87.csv', '设备200-TEST88.csv', '设备200-TEST89.csv', '设备200-TEST90.csv', '设备212-TEST91.csv', '设备212-TEST92.csv', '设备212-TEST93.csv', '设备212-TEST94.csv', '设备212-TEST95.csv', '设备212-TEST96.csv', '设备212-TEST97.csv', '设备212-TEST98.csv', '设备212-TEST99.csv', '设备212-TEST100.csv', '设备225-TEST101.csv', '设备225-TEST102.csv', '设备225-TEST103.csv', '设备225-TEST104.csv', '设备225-TEST105.csv', '设备225-TEST106.csv', '设备225-TEST107.csv', '设备225-TEST108.csv', '设备225-TEST109.csv', '设备225-TEST110.csv', '设备237-TEST111.csv', '设备237-TEST112.csv', '设备237-TEST113.csv', '设备237-TEST114.csv', '设备237-TEST115.csv', '设备237-TEST116.csv', '设备237-TEST117.csv', '设备237-TEST118.csv', '设备237-TEST119.csv', '设备237-TEST120.csv', '设备249-TEST121.csv', '设备249-TEST122.csv', '设备249-TEST123.csv', '设备249-TEST124.csv', '设备249-TEST125.csv', '设备249-TEST126.csv', '设备249-TEST127.csv', '设备249-TEST128.csv', '设备249-TEST129.csv', '设备249-TEST130.csv', '设备261-TEST131.csv', '设备261-TEST132.csv', '设备261-TEST133.csv', '设备261-TEST134.csv', '设备261-TEST135.csv', '设备261-TEST136.csv', '设备261-TEST137.csv', '设备261-TEST138.csv', '设备261-TEST139.csv', '设备261-TEST140.csv', '设备261-TEST141.csv', '设备261-TEST142.csv']
    ,
    result: '',
    index: 0,
    resultArray: [],
    output: ''
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
  },
  bindPickerChange: function (e) {
    this.setData({
      index: e.detail.value
    })
    var array = ['TEST1.csv', 'TEST2.csv', 'TEST3.csv', 'TEST4.csv', 'TEST5.csv', 'TEST6.csv', 'TEST7.csv', 'TEST8.csv', 'TEST9.csv', 'TEST10.csv', 'TEST11.csv', 'TEST12.csv', 'TEST13.csv', 'TEST14.csv', 'TEST15.csv', 'TEST16.csv', 'TEST17.csv', 'TEST18.csv', 'TEST19.csv', 'TEST20.csv', 'TEST21.csv', 'TEST22.csv', 'TEST23.csv', 'TEST24.csv', 'TEST25.csv', 'TEST26.csv', 'TEST27.csv', 'TEST28.csv', 'TEST29.csv', 'TEST30.csv', 'TEST31.csv', 'TEST32.csv', 'TEST33.csv', 'TEST34.csv', 'TEST35.csv', 'TEST36.csv', 'TEST37.csv', 'TEST38.csv', 'TEST39.csv', 'TEST40.csv', 'TEST41.csv', 'TEST42.csv', 'TEST43.csv', 'TEST44.csv', 'TEST45.csv', 'TEST46.csv', 'TEST47.csv', 'TEST48.csv', 'TEST49.csv', 'TEST50.csv', 'TEST51.csv', 'TEST52.csv', 'TEST53.csv', 'TEST54.csv', 'TEST55.csv', 'TEST56.csv', 'TEST57.csv', 'TEST58.csv', 'TEST59.csv', 'TEST60.csv', 'TEST61.csv', 'TEST62.csv', 'TEST63.csv', 'TEST64.csv', 'TEST65.csv', 'TEST66.csv', 'TEST67.csv', 'TEST68.csv', 'TEST69.csv', 'TEST70.csv', 'TEST71.csv', 'TEST72.csv', 'TEST73.csv', 'TEST74.csv', 'TEST75.csv', 'TEST76.csv', 'TEST77.csv', 'TEST78.csv', 'TEST79.csv', 'TEST80.csv', 'TEST81.csv', 'TEST82.csv', 'TEST83.csv', 'TEST84.csv', 'TEST85.csv', 'TEST86.csv', 'TEST87.csv', 'TEST88.csv', 'TEST89.csv', 'TEST90.csv', 'TEST91.csv', 'TEST92.csv', 'TEST93.csv', 'TEST94.csv', 'TEST95.csv', 'TEST96.csv', 'TEST97.csv', 'TEST98.csv', 'TEST99.csv', 'TEST100.csv', 'TEST101.csv', 'TEST102.csv', 'TEST103.csv', 'TEST104.csv', 'TEST105.csv', 'TEST106.csv', 'TEST107.csv', 'TEST108.csv', 'TEST109.csv', 'TEST110.csv', 'TEST111.csv', 'TEST112.csv', 'TEST113.csv', 'TEST114.csv', 'TEST115.csv', 'TEST116.csv', 'TEST117.csv', 'TEST118.csv', 'TEST119.csv', 'TEST120.csv', 'TEST121.csv', 'TEST122.csv', 'TEST123.csv', 'TEST124.csv', 'TEST125.csv', 'TEST126.csv', 'TEST127.csv', 'TEST128.csv', 'TEST129.csv', 'TEST130.csv', 'TEST131.csv', 'TEST132.csv', 'TEST133.csv', 'TEST134.csv', 'TEST135.csv', 'TEST136.csv', 'TEST137.csv', 'TEST138.csv', 'TEST139.csv', 'TEST140.csv', 'TEST141.csv', 'TEST142.csv']
    app.globalData.input_filename = array[e.detail.value]
  },
  func() {
    //var that = this
    wx.showLoading({
      title: '正在处理中'
    })
    wx.request({
      url: 'https://api.phmlearn.com/component/upload/1/92',
      method: "POST",
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      data: {
        access_token: app.globalData.access_token,
        file_name: app.globalData.input_filename,
      },
      success: function (res) {
        wx.request({
          url: 'https://api.phmlearn.com/component/upload/2/93',
          method: "POST",
          header: {
            "Content-Type": "application/x-www-form-urlencoded"
          },
          data: {
            access_token: app.globalData.access_token,
            file_name: res.data.data.file_name
          },
          success: function (res) {
            wx.request({
              url: 'https://api.phmlearn.com/component/upload/ML/model/62/127',
              method: "POST",
              header: {
                "Content-Type": "application/x-www-form-urlencoded"
              },
              data: {
                access_token: app.globalData.access_token,
                file_name: res.data.data.file_name
              },
              complete(res) {
                wx.hideLoading();
                if (res.data.status == 0) {
                  wx.showToast({
                    title: '处理成功'
                  })
                } else {
                  wx.showToast({
                    title: '处理失败',
                    icon: "none"
                  })
                };
              },
              success: function (res) {
                // that.setData({
                //   label: that.data.label.concat(res.data.data.predict)
                // })
                // console.log(that.data.label)

                // console.log(res.data.data.predict)
                // return res.data.data.predict
                app.globalData.resultArray = res.data.data.predict;
                //callback(res)
              }
            })
          }
        })
      }
    })
  },
  pre() {
    util.reqFunc_pre('https://api.phmlearn.com/component/upload/1/92',
      {
        "access_token": app.globalData.access_token,
        "file_name": app.globalData.input_filename,
      }, function (res) {
        console.log(res)
        app.globalData.output_fileName = res.data.data.file_name;
      })
  },

  fea() {
    util.reqFunc_fea('https://api.phmlearn.com/component/upload/2/93',
      {
        "access_token": app.globalData.access_token,
        "file_name": app.globalData.output_fileName,
      }, function (res) {
        console.log(res)
        app.globalData.output_fileName = res.data.data.file_name;
      })
  },

  diag() {
    util.reqFunc_diag('https://api.phmlearn.com/component/upload/ML/model/62/127',
      {
        "access_token": app.globalData.access_token,
        "file_name": app.globalData.output_fileName,
      },
      function (res) {
        console.log(res);
        app.globalData.resultArray = res.data.data.predict;
        resultArray: getApp().globalData.resultArray
        console.log(app.globalData.resultArray)
      }
    )
  },
  setdata() {
    var that = this;
    that.setData({
      result: app.globalData.resultArray[0]
    })
  },
  gotoPage: function () {
    wx.navigateTo({
      url: '/pages/function/function-inspect/function-inspect',
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  }
})