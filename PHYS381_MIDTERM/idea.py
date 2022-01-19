# while Mf >= 0: #while the rocket has fuel
#     dm = fuel_rate * t
#     t = t + dt
#     t_list.append(round(t, 2)) #delete the round if necessary
#     v_list.append(V)
#     fdrag = 0.5 * P * C * A * (V**2)
#     fthrust = V * (dm/dt)
#     fg = Mt * g
#     acceleration = (fthrust-fdrag-fg)/Mt
#     V = V  + acceleration * dt
#     h_list.append(h + V*dt)
#     print(V)
#     Mf = Mf - dm
#     Mt = Mt - Mf

dm = fuel_rate * t
    fThrust = (2050) * (dm / dt)
    fG = 9.8 * Mt
    print(fG)
    fDrag = 0.5 * P * C * A * V*2
    acceleration = (fThrust - fG - fDrag)/Mt
    dV = acceleration * dt
    V += dV
    h = h + (dt*V)
    Mf = Mf - dm
    Mt = Mt - Mf
    t = round(t + dt, 2)
    tt.append(t)
    hh.append(h)
    vv.append(V)