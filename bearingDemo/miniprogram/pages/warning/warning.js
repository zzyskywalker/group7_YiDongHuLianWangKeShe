// miniprogram/pages/warning/warning.js
var util = require('../../util/util.js')
var app = getApp()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    i: 0,
    time: '',
    timer: '',
    timer2: '',
    device: [],
    label: [],
    filename: ['TEST11.csv', 'TEST12.csv', 'TEST13.csv', 'TEST14.csv', 'TEST15.csv', 'TEST16.csv', 'TEST17.csv', 'TEST18.csv', 'TEST19.csv', 'TEST20.csv'],
    filename: {
      b100: ['TEST1.csv', 'TEST2.csv', 'TEST3.csv', 'TEST4.csv', 'TEST5.csv', 'TEST6.csv', 'TEST7.csv', 'TEST8.csv', 'TEST9.csv', 'TEST10.csv'],
      b108: ['TEST11.csv', 'TEST12.csv', 'TEST13.csv', 'TEST14.csv', 'TEST15.csv', 'TEST16.csv', 'TEST17.csv', 'TEST18.csv', 'TEST19.csv', 'TEST20.csv'],
      b121: ['TEST21.csv', 'TEST22.csv', 'TEST23.csv', 'TEST24.csv', 'TEST25.csv', 'TEST26.csv', 'TEST27.csv', 'TEST28.csv', 'TEST29.csv', 'TEST30.csv']
    }

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {
    this.setData({
      time: util.formatTime(new Date())
    })
    this.setDivice(this.data.filename)
  },

  //获取预测结果（单次,调试用）
  getPredict: function(filename, callback) {
    var that = this
    wx.request({
      url: 'https://api.phmlearn.com/component/upload/1/94',
      method: "POST",
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      data: {
        access_token: app.globalData.access_token,
        file_name: filename,
      },
      success: function(res) {
        wx.request({
          url: 'https://api.phmlearn.com/component/upload/2/96',
          method: "POST",
          header: {
            "Content-Type": "application/x-www-form-urlencoded"
          },
          data: {
            access_token: app.globalData.access_token,
            file_name: res.data.data.file_name
          },
          success: function(res) {
            wx.request({
              url: 'https://api.phmlearn.com/component/upload/ML/model/61/126',
              method: "POST",
              header: {
                "Content-Type": "application/x-www-form-urlencoded"
              },
              data: {
                access_token: app.globalData.access_token,
                file_name: res.data.data.file_name
              },
              success: function(res) {
                callback(res)
              }
            })
          }
        })
      }
    })
  },
  setLabel: function(arrname) {
    var temp = []
    for (let i = 0; i < arrname.length; i++) {
      this.getPredict(arrname[i], res => {
        temp = temp.concat(res.data.data.predict)
        // console.log(temp)
      })
    }
    return temp
  },
  //获取预测结果
  getPredicts: function(filename, callback) {
    var that = this
    for (let i = 0; i < filename.length; i++) {
      // console.log('1ceng'+i)
      wx.request({
        url: 'https://api.phmlearn.com/component/upload/1/94',
        method: "POST",
        header: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        data: {
          access_token: app.globalData.access_token,
          file_name: filename[i],
        },
        success: function(res) {
          if (res.data.status == 0) {
            // console.log('2ceng'+i)
            wx.request({
              url: 'https://api.phmlearn.com/component/upload/2/96',
              method: "POST",
              header: {
                "Content-Type": "application/x-www-form-urlencoded"
              },
              data: {
                access_token: app.globalData.access_token,
                file_name: res.data.data.file_name
              },
              success: function(res) {
                if (res.data.status == 0) {
                  // console.log('3ceng'+i)
                  wx.request({
                    url: 'https://api.phmlearn.com/component/upload/ML/model/61/126',
                    method: "POST",
                    header: {
                      "Content-Type": "application/x-www-form-urlencoded"
                    },
                    data: {
                      access_token: app.globalData.access_token,
                      file_name: res.data.data.file_name
                    },
                    success: function(res) {
                      if (res.data.status == 0) {
                        // console.log('4ceng'+i)
                        callback(res)
                      }
                      // console.log(res.data.data.predict)
                      // callback(res)
                    }
                  })
                }
              }
            })
          }
        }
      })
    }

  },
  //更新设备状态
  setDivice: function(bearing) {
    var temp = [
      [],
      [],
      []
    ]
    this.startTimer()
    this.setDate()
    this.getPredicts(bearing.b100, res => {
      temp[0] = temp[0].concat(res.data.data.predict)
      // console.log(temp)
      if (temp[0].length > 129) {
        console.log(temp[0])
        this.setData({
          'device[0]': {
            key: '100号设备',
            arr: temp[0]
          }
        })
      }

    })
    this.getPredicts(bearing.b108, res => {
      temp[1] = temp[1].concat(res.data.data.predict)
      // console.log(temp)
      if (temp[1].length > 129) {
        console.log(temp[1])
        this.setData({
          'device[1]': {
            key: '108号设备',
            arr: temp[1]
          }
        })
      }

    })
    this.getPredicts(bearing.b121, res => {
      temp[2] = temp[2].concat(res.data.data.predict)
      // console.log(temp)
      if (temp[2].length > 129) {
        console.log(temp[2])
        this.setData({
          'device[2]': {
            key: '121号设备',
            arr: temp[2]
          }
        })
      }

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
        if (this.data.i <= 130) {
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
      }, 60000)
    })
  },
  closeTimer: function(time) {
    clearInterval(time)
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
   * 生命周期函数--监听页面卸载
   */
  onUnload: function() {
    clearInterval(this.data.timer2)
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