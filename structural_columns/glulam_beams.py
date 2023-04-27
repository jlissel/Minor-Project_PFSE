from dataclasses import dataclass

@dataclass
class GlulamBeam:
    length: float
    b: float
    d: float
    beam_tag: str
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
            self.length, self.b, self.d, self.fb, self.kD, self.kH, self.ksb, self.kT, self.kx, self.kL
        )


### Function
def factored_bending_capacity(L: float, b: float,d: float,f_b: float, k_D = float, k_H = float, k_sb = float, k_T = float, k_x = float, k_L = float, phi=0.9) -> float:
    F_b = f_b*k_D*k_H*k_sb*k_T
    k_zbg = (130/b)**(1/10)*(610/d)**(1/10)*(9100/L)**(1/10)
    S = b*d**2/6
    Mr_1 = phi*F_b*S*k_x*k_zbg
    Mr_2 = phi*F_b*S*k_x*k_L
    M_r = min(Mr_1, Mr_2)
    return M_r
