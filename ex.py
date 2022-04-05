money=int(input("금액을 넣어주세요:"))
add="Y"
menu={"콜라":500,"커피":400,"사이다":300,"율무차":200}
menu_list=list(menu.keys())
menu_won=list(menu.values())

while(add=="Y"):
  print("[이화네 음료수]")
  print("현재금액",money)
  for i in range(4):
    print(i+1,".",menu_list[i],"-",menu_won[i],"원")

  num=int((input("음료를 선택해주세요:")))
  money=money-menu_won[num-1]

  if(money<0):
    print("금액이 부족합니다.")
    break;
  elif(money==0):
    print("잔액은 0원입니다. 이용해주셔서 감사합니다.")
    break;
  else:
    print("잔액은 %d 원입니다." %(money))
  add=input("추가로 구매하시겠습니까?(Y/N):")
  if (add=="N"):
    print("잔액은 %d 원입니다. 이용해주셔서 감사합니다."%(money))
    break;
  