<?php
// Check if the form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = htmlspecialchars($_POST['username']);
    $password = htmlspecialchars($_POST['password']);

    // For now, just display the received data
    echo "<h2>Login Details</h2>";
    echo "Username: " . $username . "<br>";
    echo "Password: " . $password . "<br>";

    // Later, you can validate the credentials with a database
} else {
    echo "Invalid request.";
}
?>
