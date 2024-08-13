import nuke

def find_nan_pixels():
    node = nuke.selectedNode()
    
    if not node:
        nuke.message("Please select a node")
        return
    
    expr = nuke.nodes.Expression()
    expr.setInput(0, node)
    expr.knob('expr0').setValue('isnan(r) || isnan(g) || isnan(b) || isnan(a) ? 1 : 0')
    expr.knob('expr1').setValue('0')
    expr.knob('expr2').setValue('0')
    expr.knob('expr3').setValue('isnan(r) || isnan(g) || isnan(b) || isnan(a) ? 1 : 0')
    
    expr['output'].setValue('rgba')
    
    nuke.message("NaN pixel mask created. White pixels indicate NaN values. Check the new Expression node in your node graph.")

find_nan_pixels()