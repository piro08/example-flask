def run():
  import scratchattach as sa
  import requests

  
  send_scratch=[]
  AppendProp = ("", "", "", "", "", "", "", "", "", "", "FIGHT_PROP_HP",
    "FIGHT_PROP_ATTACK", "FIGHT_PROP_DEFENSE",
    "FIGHT_PROP_HP_PERCENT", "FIGHT_PROP_ATTACK_PERCENT",
    "FIGHT_PROP_DEFENSE_PERCENT", "FIGHT_PROP_CRITICAL",
    "FIGHT_PROP_CRITICAL_HURT", "FIGHT_PROP_CHARGE_EFFICIENCY",
    "FIGHT_PROP_HEAL_ADD", "FIGHT_PROP_ELEMENT_MASTERY",
    "FIGHT_PROP_PHYSICAL_ADD_HURT", "FIGHT_PROP_FIRE_ADD_HURT",
    "FIGHT_PROP_ELEC_ADD_HURT", "FIGHT_PROP_WATER_ADD_HURT",
    "FIGHT_PROP_WIND_ADD_HURT", "FIGHT_PROP_ICE_ADD_HURT",
    "FIGHT_PROP_ROCK_ADD_HURT", "FIGHT_PROP_GRASS_ADD_HURT")
  equipType = ("EQUIP_BRACER", "EQUIP_NECKLACE", "EQUIP_SHOES", "EQUIP_RING",
  "EQUIP_DRESS")

  
  headers = {

    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'

  }

  
  cloud = sa.get_tw_cloud(project_id="1067889153", purpose="cloud project backend", contact="https://scratch.mit.edu/users/piro8/")
  client = cloud.requests()


  def format_stats(number):
    str_number = str(number)
    if "." not in str_number:
      str_number = str_number + "0"
    str_number = str_number.replace('.', '')
    str_number = str_number.zfill(5)
    return str_number


  @client.request
  def get_stats(uid):
    main = []
    send_scratch=[]
    
    
    print(f"(turbowarp)Account information requested for uid {uid}.")
    url = f"https://enka.network/api/uid/{uid}"
    res = requests.get(url, headers=headers)

    print(res.status_code)
    if res.status_code == 200:
      res=res.json()
      if "avatarInfoList" in res:
        for i in range(len(res["avatarInfoList"])):
          main.append("00000000")
          for ii in range(5):
            main.append("000000")
            for iii in range(5):
             main.append("0000000")
        for i in range(len(res["avatarInfoList"])):
          main[i*31]=str(res["avatarInfoList"][i]["avatarId"])
          for ii in range(len(res["avatarInfoList"][i]["equipList"])-1):
            try:
              main[i*31+equipType.index(res["avatarInfoList"][i]["equipList"][ii]["flat"]["equipType"])*6+1]=res["avatarInfoList"][i]["equipList"][ii]["flat"]["icon"][13:18] + res["avatarInfoList"][i]["equipList"][ii]["flat"]["icon"][-1]
              main[i*31+equipType.index(res["avatarInfoList"][i]["equipList"][ii]["flat"]["equipType"])*6+2]=str(AppendProp.index(res["avatarInfoList"][i]["equipList"][ii]["flat"]["reliquaryMainstat"]["mainPropId"]))+format_stats(res["avatarInfoList"][i]["equipList"][ii]["flat"]["reliquaryMainstat"]["statValue"])
            except:
              pass
            for iii in range(4):
              try:  
                main[i*31+equipType.index(res["avatarInfoList"][i]["equipList"][ii]["flat"]["equipType"])*6+3+iii]=str(AppendProp.index(res["avatarInfoList"][i]["equipList"][ii]["flat"]["reliquarySubstats"][iii]["appendPropId"]))+format_stats(res["avatarInfoList"][i]["equipList"][ii]["flat"]["reliquarySubstats"][iii]["statValue"])
              except:
                pass
              #ここまでメイン

             
        for i in range(int(len(main)/31)):
          send_scratch.append("")
          for ii in range(31):
            send_scratch[i] = send_scratch[i] + main[i*31+ii]
          
        
        main=[]  
        for ii in range(5*len(res["avatarInfoList"])):
            main.append("0-")
        for i in range(len(res["avatarInfoList"])):
          for ii in range(len(res["avatarInfoList"][i]["equipList"]) - 1):
            try:
              temp="".join(map(str, res["avatarInfoList"][i]["equipList"][ii]["reliquary"]["appendPropIdList"]))
              temp=temp+"-"
              main[i*5+equipType.index(res["avatarInfoList"][i]["equipList"][ii]["flat"]["equipType"])]=temp
            except:
              pass
        
        for i in range(int(len(main)/5)):
          send_scratch.append("")
          for ii in range(5):
            send_scratch[-1] = send_scratch[-1] + main[i*5+ii]

      
      else:
        send_scratch.append("444")
        if "showAvatarInfoList" in res["playerInfo"]:
          for i in range(len(res["playerInfo"]["showAvatarInfoList"])):
            send_scratch[0] = send_scratch[0] + str(res["playerInfo"]["showAvatarInfoList"][i]["avatarId"])
      
      temp=res["playerInfo"]
      send_scratch.append("")
      temp2=""
      if "nickname" in temp:
        for i in temp["nickname"]:
          temp2=temp2+"&#"+str(ord(i))+";"
        else:
          send_scratch[-1]=send_scratch[-1]+temp2+"-"
      else:
        send_scratch[-1]=send_scratch[-1]+"&#;-"
      send_scratch[-1]=send_scratch[-1]+str(temp.get("level", "0"))+"-"
      send_scratch[-1]=send_scratch[-1]+str(temp.get("worldLevel", "0"))+"-"
      send_scratch[-1]=send_scratch[-1]+str(temp.get("finishAchievementNum", "0"))+"-"
      send_scratch[-1]=send_scratch[-1]+str(temp.get("towerFloorIndex", "0"))+"-"
      send_scratch[-1]=send_scratch[-1]+str(temp.get("towerLevelIndex", "0"))+"-"
    
  
    else:
      send_scratch.append(res.status_code)
  
    return send_scratch

  client.start()
