<?php  

include ("../conn/connections.php");

$sql = "UPDATE DriveMap SET BRAKE=2, LFT=0, RHT=0, FWD=0, BCK=0";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}


print "Ajax has loaded";

print $servername;

$conn->close();

?>


