# #Modify the previous code so that the robot senses red twice.

# p=[0.2, 0.2, 0.2, 0.2, 0.2]
# world=['green', 'red', 'red', 'green', 'green']
# measurements = ['red', 'green']
# motions = [1,1]
# pHit = 0.6
# pMiss = 0.2
# pExact = 0.8
# pOvershoot = 0.1
# pUndershoot = 0.1

# def sense(p, Z):
    # q=[]
    # for i in range(len(p)):
        # hit = (Z == world[i])
        # q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    # s = sum(q)
    # for i in range(len(q)):
        # q[i] = q[i] / s
    # return q

# def move(p, U):
    # q = []
    # for i in range(len(p)):
        # s = pExact * p[(i-U) % len(p)]
        # s = s + pOvershoot * p[(i-U-1) % len(p)]
        # s = s + pUndershoot * p[(i-U+1) % len(p)]
        # q.append(s)
    # return q


def localize(colors,measurements,motions,sensor_right,p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    pHit = sensor_right
    pMiss = 1-sensor_right
    pExact = p_move
    pOvershoot = (1- p_move)/2
    pUndershoot = (1- p_move)/2
    def sense(p, Z):
        q=[[0 for row in range(len(colors[0]))] for col in range(len(colors))]
        for i in range(len(p)):
            for j in range(len(p[0])):
                #print colors[i][j] , " "
                hit = (Z == colors[i][j]) 
                q[i][j] = (p[i][j] * (hit * pHit + (1-hit) * pMiss))
        #print q
        s = sum(sum(q,[]))
        #print s
        for i in range(len(q)):
            for j in range(len(p[0])):
                q[i][j] = q[i][j] / s
        return q

    def move1(p,U):
        q=[]
        for k in range(len(p)):
            q.append([])
        for i in range(len(p)):
            for j in range(len(p[i])):
                r=0
                if (U[0] == 0 and U[1] == 0):
                    #print "no motion"
                    r= 1 * p[i][j]
                else:
                    #y_effect
                    if (U[0]!=0):
                        r_success= p_move * p[(i-U[0])% len(p)][j]
                        r_fail = (1 - p_move) * p[i][j]
                        r= r_success + r_fail
                    #x_effect
                    if (U[1]!=0):
                        r_success= p_move * p[i][(j-U[1])% len(p[0])]
                        r_fail = (1 - p_move) * p[i][j]
                        r= r_success + r_fail
                q[i].append(r)
        return q     
    def move(p, U):
        #print len(p) , len(p[0])
        q=[[0 for row in range(len(colors[0]))] for col in range(len(colors))]
        for i in range(len(p)):
            for j in range(len(p[0])):
                #print colors[i][j] , " "
#                s = pExact * p[(i-U[0]) % len(p)][(j-U[1]) % len(p[0])]
#                s = s + pOvershoot * p[(i-U[0]-1) % len(p)][(j-U[1]-1) % len(p[0])]
#                s = s + pUndershoot * p[(i-U[0]+1) % len(p)][(j-U[1]+1) % len(p[0])]
                if (U[0] != 0 or U[1]!=0):
                    s= (U[0] !=0 )* (p_move*p[(i-U[0])% len(p)][j]+(1-p_move)*p[i][j])
                    s+=(U[1] !=0 )* (p_move*p[i][(j-U[1])%len(p[0])]+(1-p_move)*p[i][j])
                else:
                    s = p[i][j]
                q[i][j]=s
        return q 
    for k in range(len(measurements)):
        p = move(p, motions[k])
        p = sense(p, measurements[k])
        
    # >>> Insert your code here <<<
    
    return p

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print '[' + ',\n '.join(rows) + ']'

           

def test1():
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'G'],
              ['G', 'G', 'G']]
    measurements = ['R']
    motions = [[0,0]]
    sensor_right = 1.0
    p_move = 1.0
    p = localize(colors,measurements,motions,sensor_right,p_move)
    show(p)
#    correct_answer = (
#        [[0.0, 0.0, 0.0],
#         [0.0, 1.0, 0.0],
#         [0.0, 0.0, 0.0]])


def test2():
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R']
    motions = [[0,0]]
    sensor_right = 1.0
    p_move = 1.0
    p = localize(colors,measurements,motions,sensor_right,p_move)
    show(p)
    #    correct_answer = (
#        [[0.0, 0.0, 0.0],
#         [0.0, 0.5, 0.5],
#         [0.0, 0.0, 0.0]])

def test3():
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R']
    motions = [[0,0]]
    sensor_right = 0.8
    p_move = 1.0
    p = localize(colors,measurements,motions,sensor_right,p_move)
    show(p)
#    correct_answer = (
#        [[0.06666666666, 0.06666666666, 0.06666666666],
#         [0.06666666666, 0.26666666666, 0.26666666666],
#         [0.06666666666, 0.06666666666, 0.06666666666]])

def test4():
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0,0], [0,1]]
    sensor_right = 0.8
    p_move = 1.0
    p = localize(colors,measurements,motions,sensor_right,p_move)
    show(p)
#    correct_answer = (
#        [[0.03333333333, 0.03333333333, 0.03333333333],
#         [0.13333333333, 0.13333333333, 0.53333333333],
#         [0.03333333333, 0.03333333333, 0.03333333333]])

def test5():
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0,0], [0,1]]
    sensor_right = 1.0
    p_move = 1.0
    p = localize(colors,measurements,motions,sensor_right,p_move)
    show(p)
#    correct_answer = (
#        [[0.0, 0.0, 0.0],
#         [0.0, 0.0, 1.0],
#         [0.0, 0.0, 0.0]])

def test6():
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0,0], [0,1]]
    sensor_right = 0.8
    p_move = 0.5
    p = localize(colors,measurements,motions,sensor_right,p_move)
    show(p)
#    correct_answer = (
#        [[0.0289855072, 0.0289855072, 0.0289855072],
#         [0.0724637681, 0.2898550724, 0.4637681159],
#         [0.0289855072, 0.0289855072, 0.0289855072]])

def test7():
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0,0], [0,1]]
    sensor_right = 1.0
    p_move = 0.5
    p = localize(colors,measurements,motions,sensor_right,p_move)
    show(p)
    # displays your answer
#    correct_answer = (
#        [[0.0, 0.0, 0.0],
#         [0.0, 0.33333333, 0.66666666],
#         [0.0, 0.0, 0.0]])
    
def test8():
    colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]
    measurements = ['G','G','G','G','G']
    motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
    p = localize(colors,measurements,motions,sensor_right = 0.7, p_move = 0.8)
    show(p) 
    # For the following test case, your output should be 
# [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
#  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
#  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
#  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
# (within a tolerance of +/- 0.001 for each entry)
test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()

