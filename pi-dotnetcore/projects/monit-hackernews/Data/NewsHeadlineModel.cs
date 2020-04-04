using Microsoft.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations;

namespace monit_hackernews.Data
{
    // Database context using Entity Framework
    // https://docs.microsoft.com/en-us/ef/core/get-started/?tabs=netcore-cli
    // https://elanderson.net/2019/11/asp-net-core-3-add-entity-framework-core-to-existing-project/    
    public class NewsHeadlineContext : DbContext
    {
        public NewsHeadlineContext(DbContextOptions<NewsHeadlineContext> options) : base(options)
        {}

        public DbSet<NewsHeadlineModel> Headlines { get; set; }
    }

    // Represents an entry in the database table
    public class NewsHeadlineModel
    {
        [Key]
        public string Id { get; set; }

        [Required]
        public string Title { get; set; }

        public string Comment { get; set; }
    }
}