import QtQuick 2.0
import QtQuick.Window 2.2
import QtQuick.Layouts 1.2
import QtQuick.Controls.Imagine 2.12
import QtQuick.Controls 2.15

Window {
    visibility: Qt.WindowFullScreen
    id: mainwindow
    GridLayout {
        id: grid
        anchors.fill: parent
        columns: 4
        rows: 3

        Rectangle{
            Layout.fillHeight: true
            Layout.fillWidth: true
            ColumnLayout{
                Text {
                    id: temp1
                    text: "Датчик 1 - 10"
                    color: "green"
                }
                Text{
                    id: temp2
                    text: foo.total
                    color: "blue"
                }
                Text{
                    id: temp3
                    text: "Датчик 3 - 20"
                }
                Text{
                    id: temp4
                    text: "Датчик 4 - 20"
                }
            }
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
        }
        Rectangle {
            Layout.fillHeight: true
            Layout.fillWidth: true
            color: "red"
        }
        Rectangle {
            Layout.fillHeight: true
            Layout.fillWidth: true
            color: "blue"
        }

    }
}