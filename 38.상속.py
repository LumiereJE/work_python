# 오버라이딩 : 부모 클래스를 상속받아서 동일한 메서드에 대해 재정의해 사용하는 것
# 오버 로딩 : 동일한 메서드를 매개변수를 이용하여 여러개 만드는것 (타입이 달라야 오버로딩이 일어나는데 파이썬은 타입이랄게 없음)

# 오버 로딩 : 파이썬은 오버로딩이 없음 (데이터형이 없어서 메개 변수를 아무거나 넣어도 동작하므로 오버 로딩과 유사한 효과가 있음)
#          디폴트 매개 변수 문법이 있음

class ProtoTV:
    def __init__(self, isOn, channel, volume):
        self.isOn = isOn
        self.channel = channel
        self.volume = volume

    def set_on(self, isOn):
        self.isOn = isOn

    def set_channel(self, cnl):
        if 0 < cnl < 1000:
            self.channel = cnl
            print(f"채널을 {cnl}로 변경 하였습니다.")
        else:
            print(f"채널 설정 범위가 아닙니다.")

    def set_volume(self, vol):
        self.volume = vol

    def get_on(self):
        return self.isOn

    def get_channel(self):
        return self.channel

    def get_volume(self):
        return self.volume


class TV(ProtoTV):                                           # ProtoTV로 부터 상속을 받음
    def set_channel(self, cnl):                              # 부모가 가진 메서드를 상속받아 재정의 (오버라이딩)
        if 0 < cnl < 2000:
            self.channel = cnl
            print(f"채널을 {cnl}로 변경 하였습니다.")
        else:
            print(f"채널 설정 범위가 아닙니다.")


lg_tv = TV(False, 10, 10)
samsung_tv = TV(False, 20, 20)
samsung_tv.set_channel(1200)

proto = ProtoTV(False, 10, 10)
proto.set_channel(1000)





