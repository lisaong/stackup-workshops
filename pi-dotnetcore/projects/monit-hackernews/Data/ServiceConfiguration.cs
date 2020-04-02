
// https://www.stevebrownlee.com/asp-net-core-application-settings-in-razor/
namespace monit_hackernews.Data
{
    public interface IServiceConfiguration
    {
        string ThrottleIntervalMinutes { get; set; }

        string NewsServiceUri { get; set; }
    }

    public class ServiceConfiguration: IServiceConfiguration
    {
        public string ThrottleIntervalMinutes { get; set; }

        public string NewsServiceUri { get; set; }
    }
}