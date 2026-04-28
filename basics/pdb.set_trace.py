is_available = False
is_first_section = False
is_prev_sec_completed = True
is_prev_sec_graded = False

import pdb; pdb.set_trace()
if is_first_section:
    is_avalable = True
elif is_prev_sec_completed:
    if is_prev_sec_graded:
        is_available = True

else:
    print("Hello")
    
    
    
