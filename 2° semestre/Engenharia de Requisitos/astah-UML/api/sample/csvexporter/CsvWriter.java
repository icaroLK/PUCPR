import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.util.List;
import java.util.StringJoiner;

/**
 * Class that exports given contents in CSV format. 
 */
public class CsvWriter {

    private static final String PREFIX = "\"";
    private static final String SUFFIX = PREFIX;
    private static final String NEW_LINE = "\n";
    private String separator = ",";

    /**
     * Set CSV format separator to export.
     * @param separator separator
     */
    public void setSeparator(String separator) {
        this.separator = separator;
    }

    private List<List<String>> contents;

    private String fileName;

    /**
     * @param contents Contents to export (String List stored in List)
     * @param filePath File Path to export 
     */
    public CsvWriter(List<List<String>> contents, String filePath) {
        this.contents = contents;
        this.fileName = filePath;
    }

    /**
     * Export to File.
     * @throws IOException
     */
    public void write() throws IOException {
        File csvFile = new File(fileName);
        Writer writer = new BufferedWriter(new FileWriter(csvFile));
        writeAllLines(writer);
        writer.close();
    }

    private void writeAllLines(Writer writer) throws IOException {
        String delimiter = SUFFIX + separator + PREFIX;
        for (List<String> line : contents) {
            StringJoiner joiner = new StringJoiner(delimiter, PREFIX, SUFFIX + NEW_LINE);
            line.stream().forEach(joiner::add);
            writer.write(joiner.toString());
        }
    }
}
