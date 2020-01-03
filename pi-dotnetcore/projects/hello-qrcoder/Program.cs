using System;
using System.Drawing;

// Documentation: https://github.com/codebude/QRCoder
using QRCoder;

namespace hello_qrcoder
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            QRCodeGenerator qrGenerator = new QRCodeGenerator();
            QRCodeData qrCodeData = qrGenerator.CreateQrCode("The text which should be encoded.", 
                                        QRCodeGenerator.ECCLevel.Q);
            QRCode qrCode = new QRCode(qrCodeData);
            Bitmap qrCodeImage = qrCode.GetGraphic(20);

            Console.WriteLine("Generated QRCode!");
        }
    }
}
