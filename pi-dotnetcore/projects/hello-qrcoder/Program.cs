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
            QRCodeData qrCodeData = qrGenerator.CreateQrCode("https://news.ycombinator.com/item?id=111111", 
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
