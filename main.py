import qzone

cookie = "pgv_pvi=5378396160; RK=GFAt8KiS+L; ptcz=3d4b7a7df0e25ff1e4fbbcbf549580e6ff675c15d447eda1f82580ab022af05d; tvfe_boss_uuid=2ad3ca75899f66a0; pgv_pvid=380041414; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=47; pac_uid=1_2752805684; iip=0; o_cookie=2752805684; __Q_w_s_hat_seed=1; ptui_loginuin=2752805684; luin=o2752805684; lskey=00010000900311f3c1fbb1e137effb31b8ee9167f0c8ebd19c6154c5a8dc02b34401a913678253402da3ea61; qz_screen=1451x907; __Q_w_s__QZN_TodoMsgCnt=1; randomSeed=732678; Loading=Yes; _qpsvr_localtk=0.538608791839471; uin=o2752805684; skey=@uiUJBhiLA; p_uin=o2752805684; pt4_token=2S7cft3y24nyPD5PgDMXfNOJyhz*3ezgr6yKSWHABQk_; p_skey=-7ZWUP4FXw2vZER50Huy6*HJvhNP9cT4KGwfu6MlNdc_; pgv_info=ssid=s1035078828; 2752805684_todaycount=1; 2752805684_totalcount=394; zzpaneluin=; zzpanelkey=; rv2=8058B4B9582F97FDE4DC0030012A2833F95BE7DB70CCB5F49B; property20=FE57895B6017FE9ED304D0F7BFD9F82D8CDA9FAE492296A0CF1D924A7A49B021847B0AAE7823814E; _qz_cdn=_qzs.qq.com_qzs.qq.com"

obj = qzone.Qzone(**qzone.cookie_str_to_dict(cookie))
emotionList = obj.emotion_list(uin=2752805684)

for emotion in emotionList:
  print(emotion)