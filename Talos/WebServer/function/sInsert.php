<?php  

include ("../conn/connections.php");

$sql = "UPDATE DriveMap SET BCK=1";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}


print "Ajax has loaded";

print $servername;

$conn->close();

?>