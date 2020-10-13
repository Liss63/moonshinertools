import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Layouts 1.2
import QtQuick.Controls.Imagine 2.12
import QtQuick.Controls 2.2

Window {
    visibility: Qt.WindowFullScreen
    id: mainwindow
    GridLayout {
        id: grid
        anchors.fill: parent
        columns: 4
        rows: 3

        SensorArea{
            text: "Температура 1"
            value: mmodel.temp1
            lowtolerance: "56"
            hightolerance: "90"
        }
        SensorArea{
            text: "Температура 2"
            value: mmodel.temp2
            lowtolerance: "3"
            hightolerance: "838"
        }

        SensorArea{
            text: "Температура 3"
            value: mmodel.temp3
            lowtolerance: "12"
            hightolerance: "99"
        }
        SensorArea{
            text: "Температура 4"
            value: mmodel.temp4
            lowtolerance: "33"
            hightolerance: "88"
        }
        SensorArea{
            text: "Напряжение"
            value: mmodel.voltage
            lowtolerance: "0"
            hightolerance: "220"
        }
        Rectangle {
            Layout.fillHeight: true
            Layout.fillWidth: true
            color: "red"
            TextInput {
                id: myInput
                text: foo.total
                cursorVisible: false
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                Binding {
                    target: foo
                    property: "total"
                    value: myInput.text
                }
                //onTextChanged:{
                //    foo.total = text
                //}
            }
        }
        Rectangle {
            Layout.fillHeight: true
            Layout.fillWidth: true
            Text {
                id: slTV
                text: Math.round(foo.voltage * 220)
            }
            Slider {
                id: sl
                value: foo.voltage
                Layout.fillWidth: true
                //anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                anchors.right: parent.right
                Binding {
                    target: foo
                    property: "voltage"
                    value: sl.value
                }
            }

        }

        Rectangle {
            Layout.fillHeight: true
            Layout.fillWidth: true
            color: "red"
        }
        Rectangle {
            Layout.fillHeight: true
            Layout.fillWidth: true
            color: "red"
        }
        Rectangle {
            Layout.fillHeight: true
            Layout.fillWidth: true
            color: "red"
            Button{
                id: changeValue
                text: "Установить значение"
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                onClicked: {
                    foo.total = "start"
                    foo.voltage = 0.5
                }
            }
        }

        Rectangle {
            Layout.fillHeight: true
            Layout.fillWidth: true

        }
        Rectangle {
            Layout.fillHeight: true
            Layout.fillWidth: true
            color: "red"
        }

    }
}