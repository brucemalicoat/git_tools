CREATE TABLE [MachineLearning].[TrainedModels]
(
  ModelID int identity(1,1) primary key,
  ModelName nvarchar(500),
  SourceQuery nvarchar(max),
  Metadata nvarchar(max),
  Model varbinary(max),
  TrainedDate datetime2 default getdate(),
  PredictQuery nvarchar(max)
)
go

CREATE UNIQUE NONCLUSTERED INDEX[idx_machinelearning] on [machinelearning].[trainedmodels](modelname)
GO