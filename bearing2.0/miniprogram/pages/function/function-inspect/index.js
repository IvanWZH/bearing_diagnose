// miniprogram/pages/index/index.js
var util = require('../../util/util.js')
var app = getApp()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    index: 0,
    array: ['108号设备', '121号设备'],
    result: [],
    i: 0,
    time: '',
    timer: '',
    timer2: ''

  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {
    this.setDatas(108)
    this.setData({
      time: util.formatTime(new Date()),
    })
  },


  //获取数据
  getDatas: function(bearingId, atr, callback) {
    var that = this
    wx.request({
      url: 'https://api.phmlearn.com/component/data/zhoucheng',
      method: 'POST',
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      data: {
        access_token: app.globalData.access_token,
        divice_id: bearingId,
        atrribute: atr
      },
      success: function(res) {
        callback(res)
      }
    })
  },
  setArrData: function(arr) {
    for (let i = 0; i < arr.length; i++) {
      arr[i] = arr[i].toFixed(5)
    }
    return arr
  },
  setDatas: function(bearingId) {
    this.startTimer()
    this.setDate()
    this.getDatas(bearingId, 'DE_time', res => {
      this.setData({
        'result[0]': {
          key: '驱动端振动信号',
          max: Math.max(...res.data.data.data).toFixed(5),
          min: Math.min(...res.data.data.data).toFixed(5),
          arr: this.setArrData(res.data.data.data)
        }
      })
    })
    this.getDatas(bearingId, 'FE_time', res => {
      this.setData({
        'result[1]': {
          key: '风扇端振动信号',
          max: Math.max(...res.data.data.data).toFixed(5),
          min: Math.min(...res.data.data.data).toFixed(5),
          arr: this.setArrData(res.data.data.data)
        }
      })
    })
  },

  //设置时间
  setDate: function() {
    this.setData({
      timer2: setInterval(() => {
        this.setData({
          time: util.formatTime(new Date())
        })
      }, 1000)
    })
  },
  startTimer: function() {
    this.setData({
      i: 0
    })
    this.setData({
      timer: setInterval(() => {
        if (this.data.i <= 3000) {
          this.setData({
            i: this.data.i + 1
          })
        } else {
          this.setData({
            i: 0
          })
          this.closeTimer(this.data.timer)
          this.closeTimer(this.data.timer2)
        }
      }, 1000)
    })
  },
  closeTimer: function(time) {
    clearInterval(time)
  },

  //变更设备
  bindPickerChange: function (e) {
    let arr = [108, 121]
    this.closeTimer(this.data.timer)
    this.closeTimer(this.data.timer2)
    this.setData({
      index: e.detail.value
    })
    let j = this.data.index
    this.setDatas(arr[j])
    // this.getOneOption(this.data.series);
  },
  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function() {
    clearInterval(this.data.timer2)
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function() {

  }
})