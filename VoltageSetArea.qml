import QtQuick 2.7
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.2

Rectangle{
    id: voltagesetarea
    property alias text: voltagelabel.text
    property alias value: sl.value
    signal valuechanged(real value)
    Layout.fillHeight: true
    Layout.fillWidth: true
    Column{
        anchors.fill: parent
        Label {
            id: voltagelabel
            minimumPointSize: 10
            font.pointSize: 50
            fontSizeMode: Text.Fit
            width: parent.width
            height: parent.height / 4
            wrapMode: Text.WordWrap
        }
        Text {
            id: voltagevalue
            text: Math.round(sl.value * 220)
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            minimumPointSize: 10
            font.pointSize: 120
            fontSizeMode: Text.Fit
            width: parent.width
            height: parent.height / 4
        }
        Slider {
                id: sl
                width: parent.width
                height: parent.height / 4
                onMoved:{
                    voltagesetarea.valuechanged(value)
                }
        }
        RowLayout{
             width: parent.width
             height: parent.height / 4

             Button{
                Layout.fillWidth: true
                Layout.fillHeight: true
                text: "-1"
                onClicked: {
                    sl.value = sl.value - 1/220
                    voltagesetarea.valuechanged(sl.value)
                }
            }
            Button{
                Layout.fillWidth: true
                Layout.fillHeight: true
                text: "-5"
                onClicked: {
                    sl.value = sl.value - 5/220
                    voltagesetarea.valuechanged(sl.value)
                }
            }
            Button{
                Layout.fillWidth: true
                Layout.fillHeight: true
                text: "-10"
                onClicked: {
                    sl.value = sl.value - 10/220
                    voltagesetarea.valuechanged(sl.value)
                }
            }
            Button{
                Layout.fillWidth: true
                Layout.fillHeight: true
                text: "+10"
                onClicked: {
                    sl.value = sl.value + 10/220
                    voltagesetarea.valuechanged(sl.value)
                }
            }
            Button{
                Layout.fillWidth: true
                Layout.fillHeight: true
                text: "+5"
                onClicked: {
                    sl.value = sl.value + 5/220
                    voltagesetarea.valuechanged(sl.value)
                }
            }
            Button{
                Layout.fillWidth: true
                Layout.fillHeight: true
                text: "+1"
                onClicked: {
                    sl.value = sl.value + 1/220
                    voltagesetarea.valuechanged(sl.value)
                }
            }
        }
    }
}
