import user_interface as view
import calc_rational_numbers as cr
import calc_complex_numbers as ccn
import loger as lg

def control_calc():
    in_line = view.get_expression()
    result = cr.calc(in_line)
    view.view_data(result, in_line)
    string_to_write = f" calc_rational_number: {in_line} = {str(result)}"
    lg.write(string_to_write)
   

def control_complex_calc():
    in_line = view.get_expression()
    result = ccn.complex_calc(in_line)
    view.view_data(result, in_line)
    string_to_write = f" calc_complex_number: {in_line} = {str(result)}"
    lg.write(string_to_write)
