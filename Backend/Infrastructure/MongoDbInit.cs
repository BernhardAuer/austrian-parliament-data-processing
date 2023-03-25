using Microsoft.Extensions.Options;
using MongoDB.Driver;
using WebApi.Models;

namespace WebApi.Infrastructure;

public static class MongoDbInit
{
    public static void CreateIndices(string connectionString, string dbName, string speechesMetaDataCollectionName)
    {
        var mongoClient = new MongoClient(connectionString);
        var mongoDatabase = mongoClient.GetDatabase(dbName);

        var speechesMetaDataCollection = mongoDatabase
            .GetCollection<SpeechesMetaData>(speechesMetaDataCollectionName);
        
        speechesMetaDataCollection.Indexes.CreateOne(
            new CreateIndexModel<SpeechesMetaData>(Builders<SpeechesMetaData>
                .IndexKeys.Text(x => x.topNr ).Text(x => x.topic),
                new CreateIndexOptions{DefaultLanguage = "german"}));
    }

}