////


def createnameKnob():
    node = nuke.thisNode()

    version_knob = node.knob('inputVersion')
    desc_knob = node.knob('descVersion')

    text_knob = nuke.String_Knob('v'+str(version_knob.value()),'v'+str(version_knob.value()))

    node.addKnob(text_knob)
    text_knob.setValue(desc_knob.value())
    text_knob.setEnabled(False)

    
if __name__ == "__main__":
    createnameKnob()


////

def toggleEnabled():
    node = nuke.thisNode()

    for i in node.knobs():
        if i.startswith('v'):
            print node[i].enabled()
            if node[i].enabled() == True:
                node[i].setEnabled(False)
            else:
                node[i].setEnabled(True)
        else:
            pass

if __name__ == "__main__":
    toggleEnabled()