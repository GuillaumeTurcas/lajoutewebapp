GlowScript 3.0 JavaScript
scene.width = 350
scene.height = 300
scene.range = 1.3
scene.title = "Widgets (buttons, etc.)\n"

var running = true

function Run(b) {
    running = !running
    if (running) b.text = "Pause"
    else b.text = "Run"
}
    
button({text:"Pause", pos:scene.title_anchor, bind:Run})

var box_object = box({visible:true})
var cone_object = cone({visible:false})
var pyramid_object = pyramid({visible:false})
var cylinder_object = cylinder({visible:false})
sphere({size:0.6*vec(1,1,1)})

var col = color.cyan
var currentobject = box_object
currentobject.color = col

function Color(c) {
    if (col.equals(color.cyan)) { // change to red
        currentobject.color = col = color.red
        c.text = "<b>Cyan</b>"
        c.color = color.cyan
        c.background = color.red
        r1.checked = false
        r2.checked = true
    } else {                     // change to cyan
        currentobject.color = col = color.cyan
        c.text = "<b>Red</b>"
        c.color = color.red
        c.background = color.cyan
        r1.checked = true
        r2.checked = false
    }
}
        
var cbutton = button({text:'<b>Red</b>', color:color.red, background:color.cyan, pos:scene.title_anchor, bind:Color})

scene.caption = "Vary the rotation speed: "

function setspeed(s) {
   wt.text = '{:1.2f}'.format(s.value)
}
   
var sl = slider({min:0.3, max:3, value:1.5, length:220, bind:setspeed, right:15})

var wt = wtext({text:'{:1.2f}'.format(sl.value)})

scene.append_to_caption(' radians/s\n')

var r1 = radio({bind:Color, checked:true, text:'Cyan'})

scene.append_to_caption('       ')

function M(m) {
   var op = currentobject.opacity
   var currentaxis = currentobject.axis
   currentobject.visible = false
   var val = m.selected
   if (val == "box") {currentobject = box_object}
   else if (val == "cone") {currentobject = cone_object}
   else if (val == "pyramid") {currentobject = pyramid_object}
   else if (val == "cylinder") {currentobject = cylinder_object}
   currentobject.color = col
   currentobject.axis = currentaxis
   currentobject.visible = true
   currentobject.opacity = op
}

menu({choices:['Choose an object', 'box', 'cone', 'pyramid', 'cylinder'], index:0, bind:M})

scene.append_to_caption('\n')

var r2 = radio({bind:Color, text:'Red'})

scene.append_to_caption('         ')

function transparency(b) {
   if (b.checked) {currentobject.opacity = 0.5}
   else {currentobject.opacity = 1}
}

checkbox({bind:transparency, text:'Transparent'})

var dt = 0.01
while (true) {
   await rate(1/dt)
   if (running) currentobject.rotate({angle:sl.value*dt, axis:vec(0,1,0)})
}