import QtQuick 2.7
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.2

Rectangle{
    id: sensorarea
    property alias text: sensorlabel.text
    property alias value: sensorvalue.text
    property alias lowtolerance: lowtolerance.text
    property alias hightolerance: hightolerance.text
    Layout.fillHeight: true
    Layout.fillWidth: true
    ColumnLayout{
        anchors.fill: parent
        Label {
            id: sensorlabel
            minimumPointSize: 10
            font.pointSize: 60
            fontSizeMode: Text.Fit
            Layout.fillWidth: true
            Layout.fillHeight: true
        }
        Text {
            id: sensorvalue
            color: "green"
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            minimumPointSize: 10
            font.pointSize: 130
            fontSizeMode: Text.Fit
            Layout.fillWidth: true
            Layout.fillHeight: true
        }
        RowLayout{
            Layout.fillWidth: true
            Layout.fillHeight: true
            Text{
                id: lowtolerance
                minimumPointSize: 10
                font.pointSize: 40
                fontSizeMode: Text.Fit
                Layout.fillWidth: true
                Layout.fillHeight: true
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }
            Text{
                id: hightolerance
                minimumPointSize: 10
                font.pointSize: 40
                fontSizeMode: Text.Fit
                Layout.fillWidth: true
                Layout.fillHeight: true
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }
        }
    }
}