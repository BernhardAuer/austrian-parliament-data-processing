namespace WebApi.Mappings;

// see https://www.parlament.gv.at/verstehen/glossare/abkuerzungen
public class AustrianParliamentAbbreviationMappings
{
    private Dictionary<string, string> SpeechTypes =>
        new()
        {
            { "c", "Contra"},
            { "p", "Pro"},
            { "el", "Erste Lesung"},
            { "rb", "Regierungsbank"},
            { "tb", "Tatsächliche Berichtigung"},
            { "ap", "ap" }, // todo: what is this?
            { "as", "Aktuelle Stunde" },
            { "bg", "Begründung" },
            { "bo", "Berichterstattung Ausschuss" }, // Berichterstattung durch die Obfrau bzw. den Obmann eines Ausschusses
            { "da", "Dringliche Anfrage" },
            { "de", "Dringlicher (Entschließungs-)Antrag" },
            { "er", "Erklärung" }, //  (Präsident:in, Regierungsmitglieder, Landeshauptleute)
            { "et", "Erwiderung" },
            { "eu", "Europäische Union" },
            {
                "gb", "Wortmeldung zur Geschäftsbehandlung"
            }, //  (siehe auch https://www.parlament.gv.at/verstehen/glossare/allgemein/index.html#geschaftsordnungsdebatte)
            { "kd", "Kurze Debatte" },
            { "rf", "rf" },  // todo: what is this?
            { "rs", "Regierungsbank Staatssekretär:in" },
            { "rv", "Regierungsvorlage" },
            { "un", "Unterzeichner:in" },
            { "wd", "Wahldebatte" },
            { "wm", "Wortmeldung" },
        };

    public string GetLongNameSpeechType(string abbreviation)
    {
        var isSuccessful = SpeechTypes.TryGetValue(abbreviation.ToLower(), out var longName);

        return (isSuccessful ? longName : abbreviation)!;
    }
    
}