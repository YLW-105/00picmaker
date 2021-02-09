def picmake():

    pic = open('image.ppm', 'w')
    pic.write('P3\n600 600\n255\n')

    for y in range(600):
        for x in range(600):
            # right cheek
            if (x - 570)**2 + (y-354)**2 < 90**2:
                r = 212
                g = 64
                b = 64
            # Eyes and nose
            elif ((x - 60)**2/45**2) + ((y-180)**2/60**2) < 1 or ((x - 450)**2/45**2) + ((y-180)**2/60**2) < 1 or ((x - 228)**2/30**2) + ((y-270)**2/15**2) < 1:
                # pupil
                if (x - 45)**2 + (y - 162)**2 < 20**2 or (x - 438)**2 + (y - 162)**2 < 20**2:
                    r = 255
                    g = 253
                    b = 208
                else:
                    r = 129
                    g = 30
                    b = 9
            # Mouth
            elif ((x - 258)**2/110**2) + ((y-408)**2/80**2) < 1:
                #Mouth outline
                if ((x - 258)**2/100**2) + ((y-408)**2/70**2) < 1:
                    r = 213
                    g = 135
                    b = 109
                else:
                    r = 129
                    g = 30
                    b = 9
            # The yellow body
            else:
                r = 225
                g = 183
                b = 73
            pic.write(str(r) + " " + str(g) + " " + str(b) + " ")
        pic.write("\n")
    pic.close()

picmake()
