<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $to_email = 'nageshv.9832@gmail.com'; // Replace with your receiving email address
    $subject = $_POST['subject'];
    $message = $_POST['message'];
    $headers = 'From: ' . $_POST['email'];

    if (mail($to_email, $subject, $message, $headers)) {
        echo 'Email sent successfully!';
    } else {
        echo 'Email could not be sent.';
    }
}
?>
