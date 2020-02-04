const bodyparser = require("body-parser");
const cors = require("cors");
const express = require("express");
const fs = require("fs");
const path = require("path");

const preprocessedDataPath = path.join(__dirname, "../dataset/preprocessed");
const processedDataPath = path.join(__dirname, "../dataset/processed");

const app = express();

app.use(bodyparser.urlencoded({ extended: true }));
app.use(bodyparser.json());
app.use(cors());
app.use(express.static("../dataset"));
app.set("views", "./views");
app.set("view engine", "ejs");

app.get("/", (req, res) => {
  const fileNames = fs.readdirSync(preprocessedDataPath);
  const processedFileNames = fs.readdirSync(processedDataPath);
  const processed = fileNames.map(fileName => {
    const baseName = fileName.split(".")[0];
    for (let processedFileName of processedFileNames) {
      if (processedFileName.split(".")[0] === baseName) {
        return true;
      }
    }
    return false;
  });
  res.render("index", { fileNames, processed });
});

app.get("/:fileName", (req, res) => {
  const { fileName = "" } = req.params;
  if (fileName.length === 0) {
    res.status(400).send("File name must be provided!");
    return;
  }
  res.render("process", { filePath: `preprocessed/${fileName}`, fileName });
});

app.post("/:fileName", (req, res) => {
  const { fileName = "" } = req.params;
  if (fileName.length === 0) {
    res.status(400).send("File name must be provided!");
    return;
  }
  const { areas = [] } = req.body;
  const fileNameWithoutExtension = path.basename(fileName, ".png");
  const filePath = path.join(processedDataPath, `${fileNameWithoutExtension}.json`);
  fs.writeFileSync(filePath, JSON.stringify({
    areas
  }));
  res.status(200).send();
});

app.listen(8080, () => {
  console.log("Processing server listening on port 8080.");
});