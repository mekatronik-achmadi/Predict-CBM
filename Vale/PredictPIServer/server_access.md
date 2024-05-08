# List Access PI Server

List Data Access:
- Intranet: https://142.40.33.208/piwebapi/dataservers/
- Azzure Virtual Desktop: 

**NOTE:** For security purpose, the AVD credential can't be shared here.

## URL Examples

- Path Pointing: https://142.40.33.208/piwebapi/points?path=\\pti-pi\U-LGS1-GB-X-PK-PK-70-AI
- Records Streaming:
    + Streaming: https://142.40.33.208/piwebapi/streams/F1DPHCUkIuz-VUGmPsx8gYVengkEQAAAUFRJLVBJXFUtTEdTMS1HQi1YLVBLLVBLLTcwLUFJ/recorded?selectedFields=Items.Timestamp;Items.Value
    + Streaming with specific key: https://142.40.33.208/piwebapi/streams/F1DPHCUkIuz-VUGmPsx8gYVengkEQAAAUFRJLVBJXFUtTEdTMS1HQi1YLVBLLVBLLTcwLUFJ/recorded?startTime=2022-03-18T09:54:52Z&endTime=2022-03-20T09:54:52Z&selectedFields=Items.Timestamp;Items.Value
    + Streaming interpolation: https://142.40.33.208/piwebapi/streams/F1DPHCUkIuz-VUGmPsx8gYVengkEQAAAUFRJLVBJXFUtTEdTMS1HQi1YLVBLLVBLLTcwLUFJ/interpolated?startTime=2022-01-18T09:54:52Z&endTime=2022-01-19T09:54:52Z&interval=10s&selectedFields=Items.Timestamp;Items.Value
    
## Pattern String

- Data Pointing:

```python
'{SERVER_ADDRESS}/points?path=\\\\{BASE_PATH}\{TAG_PATH}'
```

- Record Streaming:

```python
'{SERVER_ADDRESS}/streams/{WEB_ID}/recorded'
```

- Record Streaming with a selected field:

```python
'{SERVER_ADDRESS}/streams/{WEB_ID}/recorded?selectedFields=Items.Value'
```

- Record Streaming with multiple selected fields:

```python
'{SERVER_ADDRESS}/streams/{WEB_ID}/recorded?selectedFields=Items.Timestamp;Items.Value'
```

## Notes

- Software Analysis -> VibroSight Vision
- AVD (Azzure Virtual Desktop)
- Estimasi Data Paling Awal -> 21-11-2018 08:53

