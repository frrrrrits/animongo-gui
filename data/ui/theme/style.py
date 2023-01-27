class Style():
    
    surface_bg_on = (
    """
    QFrame#drop_shadow_frame {
	    border-radius: 10px;
	    border: 1px solid rgba(189, 189, 189, 120);
	    background-color:rgb(68, 71, 78)
    };     
    """
    )
    
    surface_bg_off = (
    """
    QFrame#drop_shadow_frame {
	    border-radius: 0px;
	    border: 0px solid rgba(189, 189, 189, 120);
	    background-color: rgb(68, 71, 78)
    };     
    """
    )
    
    rail_menu_button_style_on = (
    """
    QFrame {
	    border-radius: 23px;
	    background-color: rgb(0, 69, 141)
    }
    """
    )
    
    rail_menu_button_style_off = (
    """
    QFrame {
        border-radius: 23px;
        background-color: none
    }
    QFrame:hover {
        background-color: rgba(0, 69, 141, 54)
    }
    """
    )