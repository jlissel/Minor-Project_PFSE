from dataclasses import dataclass

@dataclass
class GlulamBeam:
    L: float
    b: float
    d: float
    fb: float
    kD: float 
    kH: float 
    ksb: float 
    kT: float 
    kx: float
    kL: float
    phi: float = 0.9
    
    def factored_bending_capacity(self) -> float:
        return factored_bending_capacity(
            self.L, self.b, self.d, self.fb, self.kD, self.kH, self.ksb, self.kT, self.kx, self.kL
        )


### Functions
def calc_kzbg(b: float, d: float, L: float) -> float:
    k_zbg = (130/b)**(1/10)*(610/d)**(1/10)*(9100/(L*1000))**(1/10)
    return k_zbg

def factored_bending_capacity(L: float, b: float, d: float, fb: float, kD: float, kH: float, ksb: float, kT: float, kx: float, kL: float, phi=0.9) -> float:
    F_b = fb*kD*kH*ksb*kT
    S = b*d**2/6
    kzbg = calc_kzbg(b,d,L)
    Mr_1 = phi*F_b*S*kx*kzbg
    Mr_2 = phi*F_b*S*kx*kL
    Mr = min(Mr_1, Mr_2)
    return Mr


