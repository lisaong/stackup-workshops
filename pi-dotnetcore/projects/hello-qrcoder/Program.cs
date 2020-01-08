using System;

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
            using (var qrCode = new AsciiQRCode(qrCodeData))
            {
                string qrCodeAsAsciiArt = qrCode.GetGraphic(1);
                Console.WriteLine(qrCodeAsAsciiArt);
            }

            Console.WriteLine("Generated QRCode!");
        }
    }
}
