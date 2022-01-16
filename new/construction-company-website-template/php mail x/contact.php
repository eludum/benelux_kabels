<?php 

use PHPMailer\PHPMailer\PHPMailer; 
use PHPMailer\PHPMailer\Exception; 

require '/home/erensas259/domains/shn-clean.be/public_html/PHPMailer/src/Exception.php'; 
require '/home/erensas259/domains/shn-clean.be/public_html/PHPMailer/src/PHPMailer.php'; 
require '/home/erensas259/domains/shn-clean.be/public_html/PHPMailer/src/SMTP.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['recaptcha_response'])) {

    // Build POST request:
    $recaptcha_url = 'https://www.google.com/recaptcha/api/siteverify';
    $recaptcha_secret = '6LevVeQUAAAAACJhp0e4IsqS0RHyI0LMy3iSdgD6';
    $recaptcha_response = $_POST['recaptcha_response'];

    // Make and decode POST request:
    $recaptcha = file_get_contents($recaptcha_url . '?secret=' . $recaptcha_secret . '&response=' . $recaptcha_response);
    $recaptcha = json_decode($recaptcha);

    // Take action based on the score returned:
    if ($recaptcha->score >= 0.5) {
        $name = $_POST['name'];
        $email = $_POST['email'];
        $subject = $_POST['subject'];
        $message = $_POST['message'];

        $subject = "Vraag van website: ".$subject;
        $body = "Nieuwe vraag van website:\n\nNaam: ".$name."\n\nEmail: ".$email."\n\nBericht: ".$message;
        $headers = "From: " . $email;

        $mail = new PHPMailer;
        $mail->SMTPSecure = 'tls';
        $mail->Username = "shn-clean@outlook.com";
        $mail->Password = "password koy bura";
        $mail->AddAddress("shn-clean@outlook.com");
        $mail->FromName = $name;
        $mail->Subject = $subject;
        $mail->Body = $body;
        $mail->Host = "smtp.live.com";
        $mail->Port = 587;
        $mail->IsSMTP();
        $mail->SMTPAuth = true;
        $mail->From = $mail->Username;
        $mail->Send();
        header( 'Location: http://shn-clean.be/succes.html' ) ;
        exit();
    } else {
        echo '<div style="font-size:1.25em;color:red">Er is iets fout gegaan, probeer opnieuw!</div>';
        exit;
    }

}

?>
