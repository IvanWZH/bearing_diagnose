function formatTime(date) {
  var year = date.getFullYear()
  var month = date.getMonth() + 1
  var day = date.getDate()

  var hour = date.getHours()
  var minute = date.getMinutes()
  var second = date.getSeconds()

  return [year, month, day].map(formatNumber).join('/') + ' ' + [hour, minute, second].map(formatNumber).join(':')
}

const formatNumber = n => {
  n = n.toString()
  return n[1] ? n : '0' + n
}

function reqFunc_getdata(divice_id,atrribute,callback){
  wx.request({
    url: 'https://api.phmlearn.com/component/data/zhoucheng',
    method: 'POST',
    header: {
      "Content-Type": "application/x-www-form-urlencoded"
    },
    data: {
      access_token: app.globalData.access_token,
      divice_id: divice_id,
      atrribute: atrribute
    },
    success: function (res) {
      callback(res)
    }
  })
}
function reqFunc_pre(url, data, callback) {
  wx.showLoading({
    title: '正在处理中',
  })
  wx.request({
    url: url,
    method: "POST",
    header: {
      "Content-Type": "application/x-www-form-urlencoded"
    },
    data: data,
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
    success(res) {
      callback(res);
    }
  })
}
function reqFunc_fea(url, data, callback) {
  wx.showLoading({
    title: '正在处理中',
  })
  wx.request({
    url: url,
    method: "POST",
    header: {
      "Content-Type": "application/x-www-form-urlencoded"
    },
    data: data,
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
    success(res) {
      callback(res);
    }
  })
}
function reqFunc_diag(url, data, callback) {
  wx.showLoading({
    title: '正在处理中',
  })
  wx.request({
    url: url,
    method: "POST",
    header: {
      "Content-Type": "application/x-www-form-urlencoded"
    },
    data: data,
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
    success(res) {
      callback(res);
    }
  })
}

module.exports = {
  formatTime: formatTime,
  reqFunc_pre: reqFunc_pre,
  reqFunc_fea: reqFunc_fea,
  reqFunc_diag: reqFunc_diag,
  reqFunc_getdata: reqFunc_getdata
  //reqFunc:reqFunc
}
