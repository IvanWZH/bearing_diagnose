var util = require('../../../utils/util.js')
import * as echarts from '../../../ec-canvas/echarts';
var initChart = null
var app = getApp()
function setOption(chart, ylist) {
  var options = {
    title: {
      left: 'center'
    },
    color: ["#37A2DA"],
    grid: {
      top: 20,
      right: 20,
      bottom: 30
    },
    tooltip: {
      show: true,
      trigger: 'axis'
    },
    xAxis: {
      type: 'category',
      boundaryGap: false,
      data: ['1', '2', '3', '4', '5', '6', '7']
    },
    yAxis: {
      x: 'center',
      type: 'value',
      splitLine: {
        lineStyle: {
          type: 'dashed'
        }
      }
    },
    series: [{
      type: 'line',
      smooth: true,
      data: ylist
    }]
  }
  chart.setOption(options);
}

Page({
  data: {
    time: '',
    array: ['100号设备','108号设备', '121号设备', '133号设备', '147号设备', '160号设备', '172号设备', '188号设备', '200号设备', '212号设备', '225号设备', '237号设备', '249号设备', '261号设备'],
    array2: ['驱动端信号', '风扇端信号', '基座加速度', '转速'],
    index: 0,
    index2: 0,
    labels: [],
    result: [],
    series: [],
    series: [1.85999, 1.91162, 1.63502, 1.78623, 1.78623, 2.02226, 2.20297],
    i: 0,
    timer: '',
    timer2: '',
    chartTimer: '',
    ec: {
      lazyLoad: true
    }
  },
  onLoad: function () {
    //this.setSeries([1,2,3,4,5])
    this.setDatas(108)
    this.setData({
      time: util.formatTime(new Date()),
    })
    this.oneComponent = this.selectComponent('#mychart-dom-line');
    this.getOneOption(this.data.series);
  },
  init_one: function (ylist) {           //初始化第一个图表
    this.oneComponent.init((canvas, width, height) => {
      const chart = echarts.init(canvas, null, {
        width: width,
        height: height
      });
      setOption(chart, ylist)  //赋值给echart图表
      this.chart = chart;
      return chart;
    });
  },
  getDatas: function (divice_id, attr, callback) {
    var that = this
    wx.request({
      url: 'https://api.phmlearn.com/component/data/zhoucheng',
      method: 'POST',
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      data: {
        access_token: app.globalData.access_token,
        divice_id: divice_id,
        atrribute: attr
      },
      success: function (res) {
        callback(res)
      }
    })
  },
  setArrData: function (arr) {
    for (let i = 0; i < arr.length; i++) {
      arr[i] = arr[i].toFixed(6)
  //    m=arr[i]
   //   abs[i] = Math.abs[m].toFixed(3)
    }
    return arr
  },
  setDatas: function (divice_id) {
    this.startTimer()
    this.setDate()
    this.getDatas(divice_id, 'DE_time', res => {
      this.setData({
        'result[0]': {
          key: '驱动信号',
          max: Math.max(...res.data.data.data).toFixed(3),
          min: Math.min(...res.data.data.data).toFixed(3),
          arr: this.setArrData(res.data.data.data),
          abs: Math.abs(...res.data.data.data).toFixed(3)
        }
      })
    })
    this.getDatas(divice_id, 'FE_time', res => {
      this.setData({
        'result[1]': {
          key: '风扇信号',
          max: Math.max(...res.data.data.data).toFixed(3),
          min: Math.min(...res.data.data.data).toFixed(3),
          arr: this.setArrData(res.data.data.data),
          abs: Math.abs(...res.data.data.data).toFixed(3)
        }
      })
    })
    this.getDatas(divice_id, 'BA_time', res => {
      this.setData({
        'result[2]': {
          key: '基座信号',
          max: Math.max(...res.data.data.data).toFixed(3),
          min: Math.min(...res.data.data.data).toFixed(3),
          arr: this.setArrData(res.data.data.data)

        }
      })
    })
    this.getDatas(divice_id, 'RPM', res => {
      this.setData({
        'result[3]': {
          key: '转速',
          max: Math.max(...res.data.data.data).toFixed(1),
          min: Math.min(...res.data.data.data).toFixed(1),
          arr: this.setArrData(res.data.data.data),
          abs: Math.abs(...res.data.data.data).toFixed(1)
        }
      })
    })
  },
  getChartdata: function (args) {
    let array = args
    let series1 = []
    for (let i = 0; i < 7; i++) {
      series1.push(array[i])
    }
    this.setData({
      series: series1
    })
  },
  getOneOption: function (series) {
    this.setData({
      ylist: series,
    })
    this.init_one(this.data.ylist)
  },
  setDate: function () {
    this.setData({
      timer2: setInterval(() => {
        this.setData({
          time: util.formatTime(new Date())
        })
      }, 1000)
    })
  },
  startTimer: function () {
    this.setData({
      i: 0
    })
    this.setData({
      timer: setInterval(() => {
        if (this.data.i <= 3000) {
          this.setData({
            i: this.data.i + 1
          })
        }
        else {
          this.setData({
            i: 0
          })
          this.closeTimer(this.data.timer)
          this.closeTimer(this.data.timer2)
        }
      }, 1000)
    })
  },
  closeTimer: function (time) {
    clearInterval(time)
  },
  bindPickerChange: function (e) {
    let arr = [100,108,121,133,147,160,172,188,200,212,225,249,261]
    this.closeTimer(this.data.timer)
    this.closeTimer(this.data.timer2)
    this.setData({
      index: e.detail.value
    })
    let j = this.data.index
    this.setDatas(arr[j])
    this.getOneOption(this.data.series);
  },
  bindPickerChange2: function (e) {
    this.setData({
      index2: e.detail.value
    })
    let index = e.detail.value
    let arr = this.data.result[index].arr
    this.getChartdata(arr)
    this.getOneOption(this.data.series)
  },
/*
  getLabel: function (fanid) {
    if (!wx.cloud) {
      console.error('请使用 2.2.3 或以上的基础库以使用云能力')
    } else {
      wx.cloud.init({
        traceUser: true,
      })
    }
    wx.cloud.callFunction({
      name: 'fns',
      data: {
        id: fanid
      }
    }).then(res => {
      this.setData({
        labels: res.result.data
      })
    })
  },
  */
  onUnload: function () {
    clearInterval(this.data.timer2)
  }
})