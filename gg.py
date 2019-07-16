def generate_p_smooth(p, MAX_LIMIT):     
    
    global p_smooth 
      
    for i in range(2, MAX_LIMIT + 1): 
        if maxPrimeDivisor(i) <= p: 
         
            p_smooth.append(i) 
  
