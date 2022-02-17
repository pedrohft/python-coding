resource "aws_glue_job" "job_pyspark" {
  name     = "job_desafio_modulo_um"
  role_arn = aws_iam_role.glue_role.arn

  command {
    script_location = "s3://${aws_s3_bucket.dl.bucket}/${aws_s3_bucket_object.job.key}"
  }
}
