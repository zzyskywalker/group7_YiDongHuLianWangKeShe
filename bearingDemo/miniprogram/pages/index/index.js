// miniprogram/pages/index/index.js
var util = require('../../util/util.js')
var app = getApp()
import * as echarts from '../../ec-canvas/echarts'
var initChart = null

function setOption(chart, ylist) {
  var options = {
    title: {
      left: 'center'
    },
    color: ["#37A2DA"],
    grid: {
      top: 20,
      left: 40,
      right: 40,
      bottom: 20
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

  /**
   * 页面的初始数据
   */
  data: {
    index: 0,
    array: ['100号设备', '108号设备', '121号设备'],
    result: [],
    i: 0,
    time: '',
    timer: '',
    timer2: '',
    index2: 0,
    array2: ['驱动端信号', '风扇端信号'],
    series: [-0.05966, -0.06362, -0.02712, 0.00271, -0.00959, -0.05382, -0.09053],
    chartTimer: '',
    ec: {
      lazyLoad: true
    }
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {
    this.setDatas(108)
    this.setData({
      time: util.formatTime(new Date()),
    })
    this.oneComponent = this.selectComponent('#mychart-dom-line')
    this.getOneOption(this.data.series)
  },

  //变更设备
  bindPickerChange: function(e) {
    let arr = [100, 108, 121]
    this.closeTimer(this.data.timer)
    this.closeTimer(this.data.timer2)
    this.setData({
      index: e.detail.value
    })
    let j = this.data.index
    this.setDatas(arr[j])
    this.getOneOption(this.data.series);
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
          arr: this.setArrData(res.data.data.data)
        }
      })
    })
    this.getDatas(bearingId, 'FE_time', res => {
      this.setData({
        'result[1]': {
          key: '风扇端振动信号',
          arr: this.setArrData(res.data.data.data)
        }
      })
    })
    this.getDatas(bearingId, 'RPM', res => {
      this.setData({
        'result[2]': {
          key: '工作转速',
          arr: this.setArrData(res.data.data.data)
        }
      })
    })
  },

  //图表
  bindPickerChange2: function(e) {
    this.setData({
      index2: e.detail.value
    })
    let index = e.detail.value
    let arr = this.data.result[index].arr
    this.getChartdata(arr)
    this.getOneOption(this.data.series)
  },
  init_one: function(ylist) { //初始化第一个图表
    this.oneComponent.init((canvas, width, height) => {
      const chart = echarts.init(canvas, null, {
        width: width,
        height: height
      });
      setOption(chart, ylist) //赋值给echart图表
      this.chart = chart;
      return chart;
    });
  },
  getChartdata: function(args) {
    let array = args
    let series1 = []
    for (let i = 0; i < 7; i++) {
      series1.push(array[i])
    }
    this.setData({
      series: series1
    })
  },

  getOneOption: function(series) {
    this.setData({
      ylist: series
    })
    this.init_one(this.data.ylist)
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