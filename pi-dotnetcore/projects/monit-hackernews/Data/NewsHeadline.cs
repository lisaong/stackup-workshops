using System;

namespace monit_hackernews.Data
{
    public class NewsHeadline
    {
        public DateTime Date { get; set; }

        public int Score { get; set; }

        public string Title { get; set; }

        public Uri Url { get; set; }
    }
}
