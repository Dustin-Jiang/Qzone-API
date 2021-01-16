import qzone

cookie = "pgv_pvi=5378396160; RK=GFAt8KiS+L; ptcz=3d4b7a7df0e25ff1e4fbbcbf549580e6ff675c15d447eda1f82580ab022af05d; tvfe_boss_uuid=2ad3ca75899f66a0; pgv_pvid=380041414; pac_uid=1_2752805684; iip=0; o_cookie=2752805684; ptui_loginuin=2752805684; luin=o2752805684; lskey=00010000900311f3c1fbb1e137effb31b8ee9167f0c8ebd19c6154c5a8dc02b34401a913678253402da3ea61; pgv_info=ssid=s1366455322; _qpsvr_localtk=0.08706155520930359; uin=o2752805684; skey=@OX8UFE2Vc"

qzone = qzone.Qzone(**qzone.cookie_str_to_dict(cookie))
emotion = qzone.emotion_list(uin='2752805684')
print(emotion)